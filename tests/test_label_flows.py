"""
Wave 0 stubs — Label Flows + Docs + Pre-Requirements (Phase 03)
================================================================
test_manual_label_flow_plan is active (LABEL-01).
All other 16 functions are Wave 0 stubs activated in later plans.
Skip reason format: "Wave 0 stub — activated in later plans"
"""
import pytest


def test_manual_label_flow_plan():
    """LABEL-01: the workflow guide pins the real WooCommerce single-label steps."""
    from unittest.mock import MagicMock
    from pipeline.smart_ac_verifier import _plan_scenario, _Woo_WORKFLOW_GUIDE

    # The order screen is reached by URL, not by clicking through an app shell.
    assert "page=wc-orders" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must name the wc-orders admin page"
    )
    # The plugin metabox button sequence is the heart of the manual flow.
    for step in ("Generate Packages", "Calculate Rates", "Confirm Shipment", "Print Label"):
        assert step in _Woo_WORKFLOW_GUIDE, (
            f"_Woo_WORKFLOW_GUIDE must contain the '{step}' step"
        )
    # There is no app iframe in WooCommerce — the guide must say so explicitly,
    # otherwise the agent wastes steps hunting for one.
    assert "no app iframe" in _Woo_WORKFLOW_GUIDE.lower(), (
        "_Woo_WORKFLOW_GUIDE must state that WooCommerce has no app iframe"
    )

    mock_claude = MagicMock()
    mock_claude.invoke.return_value.content = """{
        "nav_clicks": [
            "navigate: orders",
            "Open the order edit screen",
            "Click Generate Packages",
            "Click Calculate Rates",
            "Click Confirm Shipment"
        ],
        "look_for": ["Print Label", "tracking number"],
        "api_to_watch": [],
        "order_action": "create_new",
        "carrier": "UPS",
        "plan": "Open the order, build packages, rate it, confirm the shipment, verify the label"
    }"""

    result = _plan_scenario(
        scenario="UPS dry ice label scenario — generate label for dry ice shipment",
        app_url="https://test-site.example.com/wp-admin/admin.php?page=ph_multi_carrier_admin_menu",
        code_ctx="",
        expert_insight="Generate the label from the WooCommerce order edit screen",
        claude=mock_claude,
    )

    assert isinstance(result, dict), "plan_scenario must return a dict"
    assert "nav_clicks" in result, "plan must have nav_clicks"
    assert "look_for" in result, "plan must have look_for"

    nav_clicks = result.get("nav_clicks", [])
    assert isinstance(nav_clicks, list) and nav_clicks, "nav_clicks must be a non-empty list"
    assert any("Confirm Shipment" in step for step in nav_clicks), (
        f"nav_clicks must reach Confirm Shipment. Got: {nav_clicks}"
    )

    look_for = result.get("look_for", [])
    assert isinstance(look_for, list)
    assert any("Print Label" in item for item in look_for), (
        f"look_for must include the Print Label evidence. Got: {look_for}"
    )


def test_auto_generate_flow():
    """LABEL-02: the guide grounds the agent in the automation repo's real locators."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    # These come straight from ups-woo-automation/src/pages/wooCommerceAdmin/ordersPage.ts.
    for locator in (
        ".button.ups_generate_packages",
        ".button.wf_ups_generate_packages_rates",
        "#wf_ups_service_select",
        ".button.ups_create_shipment",
        "a.order-view",
    ):
        assert locator in _Woo_WORKFLOW_GUIDE, (
            f"_Woo_WORKFLOW_GUIDE must carry the automation locator {locator}"
        )

    # The prefixes are UPS-plugin specific — the guide must warn, not mislead.
    assert "probe the AX tree" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must warn that ups_/wf_ups_ prefixes are plugin-specific"
    )


def test_bulk_label_flow():
    """LABEL-03: bulk labels go through the WordPress bulk-action control."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "#bulk-action-selector-top" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must name the WordPress bulk-action select"
    )
    assert "#doaction" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must name the Apply button for bulk actions"
    )
    assert ".notice.notice-success" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must say where bulk success is confirmed"
    )
    assert "Shipment accepted successfully" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must quote the per-order bulk success message"
    )
    assert "UPS-Shipping-Labels-" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must document the bulk PDF filename pattern"
    )


def test_return_label_flow():
    """LABEL-04: return labels need an order that already has a shipment."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "Generate Return Label" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must mention the Generate Return Label action"
    )
    assert "#return_label_service" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must name the return service select"
    )
    assert "Print Return Label" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must state the Print Return Label evidence"
    )
    assert "existing_fulfilled" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE must tell the planner to reuse an already-shipped order"
    )


def test_doc01_badge_check():
    """DOC-01: label existence is proved by the Print Label link and the order note."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "DOC-01" in _Woo_WORKFLOW_GUIDE
    assert "Print Label" in _Woo_WORKFLOW_GUIDE
    assert "tracking number" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-01 must reference the tracking number in the order note"
    )


def test_doc02_download_zip():
    """DOC-02: label downloads are verified by file signature, not by a ZIP bundle."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "DOC-02" in _Woo_WORKFLOW_GUIDE
    for marker in ("GIF", "%PDF", "^XA"):
        assert marker in _Woo_WORKFLOW_GUIDE, (
            f"_Woo_WORKFLOW_GUIDE DOC-02 must document the {marker} file signature"
        )
    assert "1Z[A-Z0-9]{16}" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-02 must document the UPS tracking-number pattern"
    )


def test_doc02_download_zip_handler():
    """DOC-02 handler: _do_action download_zip extracts ZIP content into action['_zip_content']."""
    import io
    import zipfile
    from unittest.mock import MagicMock, patch

    # Build an in-memory ZIP with a JSON file
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("Download Documents.json", '{"shipment_id": "123"}')
    buf.seek(0)
    zip_bytes = buf.read()

    # Mock a temporary file path that download.save_as writes the ZIP into
    import tempfile, os, shutil

    tmp_dir = tempfile.mkdtemp(prefix="test_sav_zip_")
    zip_path = os.path.join(tmp_dir, "woo_download.zip")
    with open(zip_path, "wb") as f:
        f.write(zip_bytes)

    mock_download = MagicMock()

    def fake_save_as(path):
        shutil.copy(zip_path, path)

    mock_download.save_as.side_effect = fake_save_as

    mock_dl_info = MagicMock()
    mock_dl_info.__enter__ = MagicMock(return_value=mock_dl_info)
    mock_dl_info.__exit__ = MagicMock(return_value=False)
    mock_dl_info.value = mock_download

    mock_frame = MagicMock()
    mock_el = MagicMock()
    mock_el.count.return_value = 1
    mock_el.first = mock_el
    mock_frame.get_by_role.return_value = mock_el

    mock_page = MagicMock()
    mock_page.frames = []
    mock_page.expect_download.return_value = mock_dl_info
    mock_page.get_by_role.return_value = mock_el

    action = {"action": "download_zip", "target": "Download Documents"}

    with patch("pipeline.smart_ac_verifier._get_app_frame", return_value=mock_frame):
        from pipeline.smart_ac_verifier import _do_action
        result = _do_action(mock_page, action)

    shutil.rmtree(tmp_dir, ignore_errors=True)

    assert result is True, f"download_zip _do_action should return True, got {result}"
    assert "_zip_content" in action, "action should have '_zip_content' after download_zip"
    assert "Download Documents.json" in action["_zip_content"], (
        f"_zip_content should contain 'Download Documents.json', keys: {list(action['_zip_content'].keys())}"
    )
    assert action["_zip_content"]["Download Documents.json"]["shipment_id"] == "123", (
        f"Parsed JSON should have shipment_id='123', got: {action['_zip_content']['Download Documents.json']}"
    )


def test_doc03_how_to_zip():
    """DOC-02 handler: download_zip works with mixed content (JSON + CSV)."""
    import io
    import zipfile
    from unittest.mock import MagicMock, patch
    import tempfile, os, shutil

    # Build an in-memory ZIP with JSON + CSV files
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("data.json", '{"key": "value"}')
        zf.writestr("report.csv", "col1,col2\nval1,val2\n")
    buf.seek(0)
    zip_bytes = buf.read()

    tmp_dir = tempfile.mkdtemp(prefix="test_how_to_zip_")
    zip_path = os.path.join(tmp_dir, "woo_download.zip")
    with open(zip_path, "wb") as f:
        f.write(zip_bytes)

    mock_download = MagicMock()

    def fake_save_as(path):
        shutil.copy(zip_path, path)

    mock_download.save_as.side_effect = fake_save_as

    mock_dl_info = MagicMock()
    mock_dl_info.__enter__ = MagicMock(return_value=mock_dl_info)
    mock_dl_info.__exit__ = MagicMock(return_value=False)
    mock_dl_info.value = mock_download

    mock_frame = MagicMock()
    mock_el = MagicMock()
    mock_el.count.return_value = 1
    mock_el.first = mock_el
    mock_frame.get_by_role.return_value = mock_el

    mock_page = MagicMock()
    mock_page.frames = []
    mock_page.expect_download.return_value = mock_dl_info
    mock_page.get_by_role.return_value = mock_el

    action = {"action": "download_zip", "target": "Download"}

    with patch("pipeline.smart_ac_verifier._get_app_frame", return_value=mock_frame):
        from pipeline.smart_ac_verifier import _do_action
        result = _do_action(mock_page, action)

    shutil.rmtree(tmp_dir, ignore_errors=True)

    assert result is True, f"download_zip should return True for mixed ZIP, got {result}"
    assert "_zip_content" in action
    content = action["_zip_content"]
    assert "data.json" in content, f"JSON file should be in _zip_content, keys={list(content.keys())}"
    assert "report.csv" in content, f"CSV file should be in _zip_content, keys={list(content.keys())}"
    assert isinstance(content["data.json"], dict), "JSON content should be parsed as dict"
    assert isinstance(content["report.csv"], str), "CSV content should be a string"


def test_doc02_download_file_csv():
    """DOC-02 (file): download_file handler reads CSV content into _file_content."""
    import io
    import tempfile, os, shutil
    from unittest.mock import MagicMock, patch

    # Build a CSV file in a temp location
    csv_content = "col1,col2,col3\nrow1a,row1b,row1c\nrow2a,row2b,row2c\n"
    tmp_dir = tempfile.mkdtemp(prefix="test_sav_file_")
    csv_path = os.path.join(tmp_dir, "report.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(csv_content)

    mock_download = MagicMock()
    mock_download.suggested_filename = "report.csv"

    def fake_save_as(path):
        shutil.copy(csv_path, path)

    mock_download.save_as.side_effect = fake_save_as

    mock_dl_info = MagicMock()
    mock_dl_info.__enter__ = MagicMock(return_value=mock_dl_info)
    mock_dl_info.__exit__ = MagicMock(return_value=False)
    mock_dl_info.value = mock_download

    mock_frame = MagicMock()
    mock_el = MagicMock()
    mock_el.count.return_value = 1
    mock_el.first = mock_el
    mock_frame.get_by_role.return_value = mock_el

    mock_page = MagicMock()
    mock_page.frames = []
    mock_page.expect_download.return_value = mock_dl_info
    mock_page.get_by_role.return_value = mock_el

    action = {"action": "download_file", "target": "Export CSV"}

    with patch("pipeline.smart_ac_verifier._get_app_frame", return_value=mock_frame):
        from pipeline.smart_ac_verifier import _do_action
        result = _do_action(mock_page, action)

    shutil.rmtree(tmp_dir, ignore_errors=True)

    assert result is True, f"download_file _do_action should return True, got {result}"
    assert "_file_content" in action, "action should have '_file_content' after download_file"
    fc = action["_file_content"]
    assert isinstance(fc, dict), f"_file_content should be a dict, got {type(fc)}"
    assert "headers" in fc, f"_file_content must have 'headers' key, keys={list(fc.keys())}"
    assert "row_count" in fc, f"_file_content must have 'row_count' key, keys={list(fc.keys())}"
    assert "sample_rows" in fc, f"_file_content must have 'sample_rows' key, keys={list(fc.keys())}"
    assert fc["headers"] == ["col1", "col2", "col3"], f"Unexpected headers: {fc['headers']}"
    assert fc["row_count"] == 2, f"Expected 2 data rows, got {fc['row_count']}"


def test_doc03_label_request_xml():
    """DOC-03: the shipment request/response render as the first two <pre> blocks."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "DOC-03" in _Woo_WORKFLOW_GUIDE
    assert "<pre>" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-03 must say the logs render in <pre> blocks"
    )
    assert "not a download" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-03 must stop the agent trying to download the log"
    )


def test_doc04_print_documents():
    """DOC-04: package counts are read off the plugin's package table."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "DOC-04" in _Woo_WORKFLOW_GUIDE
    assert "#wf_ups_package_list tbody tr" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-04 must name the package-row locator"
    )
    assert "total row" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-04 must warn that the last row is a total"
    )


def test_doc05_rate_log():
    """DOC-05: rate evidence must be captured before the shipment is confirmed."""
    from pipeline.smart_ac_verifier import _Woo_WORKFLOW_GUIDE

    assert "DOC-05" in _Woo_WORKFLOW_GUIDE
    assert "before" in _Woo_WORKFLOW_GUIDE and "Confirm Shipment" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-05 must order rate capture before Confirm Shipment"
    )
    assert "replaced by the shipment result" in _Woo_WORKFLOW_GUIDE, (
        "_Woo_WORKFLOW_GUIDE DOC-05 must explain why the ordering matters"
    )


def test_pre01_dry_ice_preconditions():
    """PRE-01: dry ice preconditions include Woo AppProducts nav + enable toggle + CLEANUP as list item."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="dry ice shipment", carrier="fedex")
    assert isinstance(steps, list), f"_get_preconditions must return a list, got {type(steps)}"

    # Must include the Is Dry Ice Needed toggle step
    has_dry_ice_toggle = any("Is Dry Ice Needed" in s for s in steps)
    assert has_dry_ice_toggle, (
        f"PRE-01 steps must contain 'Is Dry Ice Needed' toggle step. Steps: {steps}"
    )

    # Must include a CLEANUP step as a list item (not just a comment string)
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-01 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )
    has_cleanup_dry_ice = any(
        "Is Dry Ice Needed" in s or "uncheck" in s.lower() or "dry ice" in s.lower()
        for s in cleanup_steps
    )
    assert has_cleanup_dry_ice, (
        f"PRE-01 CLEANUP step must mention 'Is Dry Ice Needed' or 'uncheck'. Cleanup steps: {cleanup_steps}"
    )


def test_pre02_alcohol_preconditions():
    """PRE-02: alcohol preconditions include Woo AppProducts nav + Is Alcohol + CLEANUP as list item."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="alcohol shipment", carrier="fedex")
    assert isinstance(steps, list)

    # Must include the Is Alcohol toggle step
    has_alcohol_toggle = any("Is Alcohol" in s for s in steps)
    assert has_alcohol_toggle, (
        f"PRE-02 steps must contain 'Is Alcohol' toggle step. Steps: {steps}"
    )

    # Must include a CLEANUP step referencing Is Alcohol
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-02 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )
    has_cleanup_alcohol = any(
        "Is Alcohol" in s or "alcohol" in s.lower()
        for s in cleanup_steps
    )
    assert has_cleanup_alcohol, (
        f"PRE-02 CLEANUP step must mention 'Is Alcohol'. Cleanup steps: {cleanup_steps}"
    )


def test_pre03_battery_preconditions():
    """PRE-03: battery preconditions include Woo AppProducts nav + Is Battery/Dangerous Good + CLEANUP."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="battery shipment", carrier="fedex")
    assert isinstance(steps, list)

    # Must include Is Battery or Dangerous Good toggle step
    has_battery_toggle = any(
        "Is Battery" in s or "Dangerous Good" in s for s in steps
    )
    assert has_battery_toggle, (
        f"PRE-03 steps must contain 'Is Battery' or 'Dangerous Good' toggle step. Steps: {steps}"
    )

    # Must include a CLEANUP step
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-03 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )


def test_pre04_signature_preconditions():
    """PRE-04: signature preconditions include Woo AppProducts nav + Signature field + CLEANUP."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="signature required shipment", carrier="fedex")
    assert isinstance(steps, list)

    # Must include a Signature field step
    has_signature_step = any("Signature" in s for s in steps)
    assert has_signature_step, (
        f"PRE-04 steps must contain a 'Signature' step. Steps: {steps}"
    )

    # Must include a CLEANUP step
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-04 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )


def test_pre05_hal_preconditions():
    """PRE-05: HAL preconditions include AppProducts nav + Hold at Location + CLEANUP. No SideDock."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="hold at location shipment", carrier="fedex")
    assert isinstance(steps, list), f"_get_preconditions must return a list, got {type(steps)}"

    # Must include Hold at Location step
    has_hal_step = any("Hold at Location" in s for s in steps)
    assert has_hal_step, (
        f"PRE-05 steps must contain 'Hold at Location' step. Steps: {steps}"
    )

    # Must reference AppProducts hamburger nav (no SideDock in Woo)
    has_nav = any(
        "hamburger" in s.lower() or "Products" in s
        for s in steps
    )
    assert has_nav, (
        f"PRE-05 steps must reference AppProducts navigation (hamburger or Products). Steps: {steps}"
    )

    # Must include a CLEANUP step
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-05 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )

    # Must NOT reference SideDock (SideDock is FedEx-only, does not exist in Woo)
    has_sidedock = any("SideDock" in s for s in steps)
    assert not has_sidedock, (
        f"PRE-05 (HAL) must NOT reference 'SideDock' — SideDock does not exist in Woo. Steps: {steps}"
    )


def test_pre06_insurance_preconditions():
    """PRE-06: insurance preconditions include AppProducts nav + Insurance/Declared Value + CLEANUP. No SideDock."""
    from pipeline.smart_ac_verifier import _get_preconditions

    steps = _get_preconditions(scenario_text="insurance coverage shipment", carrier="fedex")
    assert isinstance(steps, list), f"_get_preconditions must return a list, got {type(steps)}"

    # Must include Insurance or Declared Value step
    has_insurance_step = any("Insurance" in s or "Declared Value" in s for s in steps)
    assert has_insurance_step, (
        f"PRE-06 steps must contain 'Insurance' or 'Declared Value' step. Steps: {steps}"
    )

    # Must reference AppProducts hamburger nav (no SideDock in Woo)
    has_nav = any(
        "hamburger" in s.lower() or "Products" in s
        for s in steps
    )
    assert has_nav, (
        f"PRE-06 steps must reference AppProducts navigation (hamburger or Products). Steps: {steps}"
    )

    # Must include a CLEANUP step
    cleanup_steps = [s for s in steps if s.startswith("(CLEANUP")]
    assert len(cleanup_steps) > 0, (
        f"PRE-06 steps must include at least one (CLEANUP ...) list item. Steps: {steps}"
    )

    # Must NOT reference SideDock (SideDock is FedEx-only, does not exist in Woo)
    has_sidedock = any("SideDock" in s for s in steps)
    assert not has_sidedock, (
        f"PRE-06 (Insurance) must NOT reference 'SideDock' — SideDock does not exist in Woo. Steps: {steps}"
    )


def test_label05_dangerous_products(tmp_path):
    """LABEL-05: create_order with use_dangerous_products=True uses DANGEROUS_PRODUCTS_JSON."""
    from unittest.mock import MagicMock, patch

    env_file = tmp_path / "test-carrier.env"
    env_file.write_text(
        "WOO_SITE_URL=https://qa.example.com\n"
        "WOO_CONSUMER_KEY=ck_fake\n"
        "WOO_CONSUMER_SECRET=cs_fake\n"
        "WOO_API_VERSION=wc/v3\n"
        'SIMPLE_PRODUCTS_JSON=[{"product_id": 100, "variation_id": 1001}]\n'
        'DANGEROUS_PRODUCTS_JSON=[{"product_id": 200, "variation_id": 2002}]\n',
        encoding="utf-8",
    )

    fake_client = MagicMock()
    fake_client.create_order.return_value = {"id": 8888, "number": "8888"}

    with patch("pipeline.order_creator._client_for_env", return_value=fake_client):
        from pipeline.order_creator import create_order

        assert create_order(env_file, use_dangerous_products=True) == "8888"
        line_items = fake_client.create_order.call_args[0][0]["line_items"]
        assert len(line_items) == 1
        assert line_items[0]["product_id"] == 200
        assert line_items[0]["variation_id"] == 2002, (
            "Expected the dangerous-goods product from DANGEROUS_PRODUCTS_JSON"
        )

        fake_client.create_order.reset_mock()
        fake_client.create_order.return_value = {"id": 7777, "number": "7777"}
        assert create_order(env_file, use_dangerous_products=False) == "7777"
        line_items2 = fake_client.create_order.call_args[0][0]["line_items"]
        assert line_items2[0]["product_id"] == 100
        assert line_items2[0]["variation_id"] == 1001, (
            "Expected the simple product from SIMPLE_PRODUCTS_JSON"
        )


