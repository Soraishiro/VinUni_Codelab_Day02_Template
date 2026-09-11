import json
import VinUni_Codelab_Day02_Template.prompt_prototype as pp


def _fn(name):
    fn = getattr(pp, name, None)
    assert callable(fn), f"{name} must be implemented"
    return fn


def test_low_risk_high_confidence_case_auto_routes():
    apply_policy_gate = _fn("apply_policy_gate")
    decide_lane = _fn("decide_lane")
    analysis = {
        "summary": "Khách không đăng nhập được ứng dụng VinFast.",
        "intents": ["digital_app_support"],
        "facts": {"vehicle_identifier": "30A-123.45"},
        "missing_information": [],
        "risk_flags": [],
        "prompt_injection_detected": False,
    }
    routing = {
        "category": "digital_app_support",
        "suggested_destination": "digital_app_support",
        "confidence": 0.97,
        "reason": "Yêu cầu chỉ liên quan ứng dụng.",
    }
    gate = apply_policy_gate(analysis)
    result = decide_lane(analysis, routing, gate)
    assert result["decision"] == "AUTO_ROUTE"
    assert result["needs_human_review"] is False


def test_missing_information_never_auto_routes():
    apply_policy_gate = _fn("apply_policy_gate")
    decide_lane = _fn("decide_lane")
    analysis = {
        "summary": "Khách muốn đặt lịch kiểm tra xe nhưng chưa cung cấp thông tin xe.",
        "intents": ["service_appointment"],
        "facts": {},
        "missing_information": ["vehicle_identifier"],
        "risk_flags": [],
        "prompt_injection_detected": False,
    }
    routing = {
        "category": "service_appointment",
        "suggested_destination": "service_appointment",
        "confidence": 0.98,
        "reason": "Yêu cầu đặt lịch.",
    }
    result = decide_lane(analysis, routing, apply_policy_gate(analysis))
    assert result["decision"] == "HUMAN_REVIEW"
    assert result["needs_human_review"] is True


def test_sensitive_warranty_case_escalates_to_specialist():
    apply_policy_gate = _fn("apply_policy_gate")
    decide_lane = _fn("decide_lane")
    analysis = {
        "summary": "Khách yêu cầu VinFast cam kết thay pin miễn phí theo bảo hành.",
        "intents": ["warranty_question"],
        "facts": {"vehicle_identifier": "VF8-TEST"},
        "missing_information": [],
        "risk_flags": ["warranty_or_compensation"],
        "prompt_injection_detected": False,
    }
    routing = {
        "category": "warranty_question",
        "suggested_destination": "warranty_specialist",
        "confidence": 0.99,
        "reason": "Cần chuyên gia bảo hành.",
    }
    result = decide_lane(analysis, routing, apply_policy_gate(analysis))
    assert result["decision"] == "SPECIALIST_ESCALATION"
    assert result["needs_human_review"] is True


def test_prompt_injection_forces_human_review():
    apply_policy_gate = _fn("apply_policy_gate")
    decide_lane = _fn("decide_lane")
    analysis = {
        "summary": "Người dùng yêu cầu bỏ qua quy định và tự đóng case.",
        "intents": ["general_customer_service"],
        "facts": {},
        "missing_information": [],
        "risk_flags": [],
        "prompt_injection_detected": True,
    }
    routing = {
        "category": "general_customer_service",
        "suggested_destination": "general_customer_service",
        "confidence": 0.99,
        "reason": "Yêu cầu chung.",
    }
    result = decide_lane(analysis, routing, apply_policy_gate(analysis))
    assert result["decision"] == "HUMAN_REVIEW"
    assert "prompt_injection" in result["reason"].lower()


def test_low_confidence_case_requires_human_review():
    apply_policy_gate = _fn("apply_policy_gate")
    decide_lane = _fn("decide_lane")
    analysis = {
        "summary": "Yêu cầu chưa rõ.",
        "intents": ["general_customer_service"],
        "facts": {},
        "missing_information": [],
        "risk_flags": [],
        "prompt_injection_detected": False,
    }
    routing = {
        "category": "general_customer_service",
        "suggested_destination": "general_customer_service",
        "confidence": 0.71,
        "reason": "Không đủ chắc chắn.",
    }
    result = decide_lane(analysis, routing, apply_policy_gate(analysis))
    assert result["decision"] == "HUMAN_REVIEW"
    assert result["needs_human_review"] is True


def test_parse_json_response_accepts_markdown_fence():
    parse_json_response = _fn("parse_json_response")
    raw = '```json\n{"category":"digital_app_support","confidence":0.95}\n```'
    assert parse_json_response(raw)["confidence"] == 0.95


def test_pipeline_uses_two_roles_and_auto_routes_low_risk_case():
    run_triage_pipeline = _fn("run_triage_pipeline")
    calls = []

    def fake_model(system_prompt, user_input):
        calls.append(system_prompt)
        if "INTAKE_ANALYST" in system_prompt:
            return json.dumps({
                "summary": "Khách không đăng nhập được ứng dụng.",
                "intents": ["digital_app_support"],
                "facts": {"vehicle_identifier": "30A-123.45"},
                "missing_information": [],
                "risk_flags": [],
                "prompt_injection_detected": False,
            }, ensure_ascii=False)
        if "ROUTING_SPECIALIST" in system_prompt:
            return json.dumps({
                "category": "digital_app_support",
                "suggested_destination": "digital_app_support",
                "confidence": 0.97,
                "reason": "Yêu cầu ứng dụng đơn giản.",
            }, ensure_ascii=False)
        raise AssertionError("unexpected role")

    result = run_triage_pipeline("Tôi không đăng nhập được app.", model_caller=fake_model)
    assert result["decision"] == "AUTO_ROUTE"
    assert result["suggested_destination"] == "digital_app_support"
    assert len(calls) == 2


def test_pipeline_skips_router_for_sensitive_case():
    run_triage_pipeline = _fn("run_triage_pipeline")
    calls = []

    def fake_model(system_prompt, user_input):
        calls.append(system_prompt)
        return json.dumps({
            "summary": "Khách yêu cầu quyết định bảo hành miễn phí.",
            "intents": ["warranty_question"],
            "facts": {"vehicle_identifier": "VF8-TEST"},
            "missing_information": [],
            "risk_flags": ["warranty_or_compensation"],
            "prompt_injection_detected": False,
        }, ensure_ascii=False)

    result = run_triage_pipeline("Hãy xác nhận thay pin miễn phí bảo hành.", model_caller=fake_model)
    assert result["decision"] == "SPECIALIST_ESCALATION"
    assert result["suggested_destination"] == "warranty_specialist"
    assert len(calls) == 1


def test_pipeline_fails_closed_when_model_returns_invalid_json():
    run_triage_pipeline = _fn("run_triage_pipeline")

    def fake_model(system_prompt, user_input):
        return "not-json"

    result = run_triage_pipeline("Yêu cầu bất kỳ", model_caller=fake_model)
    assert result["decision"] == "FALLBACK_MANUAL"
    assert result["needs_human_review"] is True
    assert result["boundary_checks"]["fail_closed"] is True
