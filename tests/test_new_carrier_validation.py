from __future__ import annotations

from pathlib import Path

from pipeline.new_carrier_validation import (
    NewCarrierValidationRun,
    WooProductRef,
    build_new_carrier_run,
    build_carrier_env_content,
    load_new_carrier_run,
    load_existing_carrier_env,
    save_new_carrier_run,
)


def test_build_carrier_env_content_uses_expected_product_env_keys():
    run = NewCarrierValidationRun(
        carrier_code="newCarrierX",
        store_name="new-carrier-store",
        app_url="https://carrier-qa.example.com/wp-admin/admin.php?page=ph_multi_carrier_admin_menu",
        woo_site_url="https://carrier-qa.example.com/wp-admin/",
        woo_consumer_secret="shpat_test",
        product_groups={
            "simple": [WooProductRef(product_id=1)],
            "variable": [WooProductRef(product_id=2, variation_id=22)],
            "digital": [WooProductRef(product_id=3)],
            "dangerous": [WooProductRef(product_id=4)],
        },
    )

    content = build_carrier_env_content(run)

    assert "CARRIER=newCarrierX" in content
    # Key names must match ups-woo-automation/env_sample exactly.
    assert "site_url=new-carrier-store" in content
    assert "CONSUMER_KEY=" in content
    assert "CONSUMER_SECRET=" in content
    assert "userName=" in content
    assert "pass=" in content
    # Only variable products carry a variation_id; simple/digital/dangerous omit it.
    assert "SIMPLE_PRODUCTS_JSON='[{\"product_id\":1}]'" in content
    assert "VARIABLE_PRODUCTS_JSON='[{\"product_id\":2,\"variation_id\":22}]'" in content
    assert "DIGITAL_PRODUCTS_JSON='[{\"product_id\":3}]'" in content
    assert "DANGEROUS_PRODUCTS_JSON='[{\"product_id\":4}]'" in content


def test_load_existing_carrier_env_returns_empty_for_missing_file():
    missing = load_existing_carrier_env("definitely-not-a-real-carrier-env")
    assert missing == {}


def test_build_new_carrier_run_persists_checkpoint_and_suite_results():
    run = build_new_carrier_run(
        carrier_code="newCarrierX",
        store_name="new-carrier-store",
        product_groups={
            "simple": [WooProductRef(product_id=1)],
            "variable": [],
            "digital": [],
            "dangerous": [],
        },
        registration_done=True,
        registration_notes="Carrier added in app and credentials verified.",
        suite_results={"smoke": {"returncode": 0}},
    )

    assert run.registration_done is True
    assert "credentials verified" in run.registration_notes
    assert run.suite_results["smoke"]["returncode"] == 0


def test_save_and_load_new_carrier_run_round_trip():
    run = build_new_carrier_run(
        carrier_code="newCarrierX",
        store_name="new-carrier-store",
        store_created=True,
        app_installed=True,
        app_url="https://carrier-qa.example.com/wp-admin/admin.php?page=ph_multi_carrier_admin_menu",
        product_groups={
            "simple": [WooProductRef(product_id=1)],
            "variable": [],
            "digital": [],
            "dangerous": [],
        },
        env_path="/tmp/newCarrierX.env",
        registration_done=True,
        registration_notes="QA completed carrier setup.",
        suite_results={"smoke": {"returncode": 0}},
    )

    path = save_new_carrier_run(run)
    loaded = load_new_carrier_run(path)

    assert loaded.carrier_code == "newCarrierX"
    assert loaded.store_name == "new-carrier-store"
    assert loaded.store_created is True
    assert loaded.app_installed is True
    assert loaded.env_path == "/tmp/newCarrierX.env"
    assert loaded.registration_done is True
    assert loaded.registration_notes == "QA completed carrier setup."
    assert loaded.suite_results["smoke"]["returncode"] == 0
    assert loaded.product_groups["simple"][0].product_id == 1
