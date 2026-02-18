"""Tests for griddy.pfr.models module."""

import pytest


@pytest.mark.unit
class TestModelsLazyLoading:
    def test_import_security(self):
        from griddy.pfr import models

        assert hasattr(models, "Security")

    def test_import_security_typed_dict(self):
        from griddy.pfr import models

        assert hasattr(models, "SecurityTypedDict")

    def test_unknown_attr_raises(self):
        from griddy.pfr import models

        with pytest.raises(AttributeError):
            _ = models.NonExistentModel

    def test_dir_lists_models(self):
        from griddy.pfr import models

        d = dir(models)
        assert "Security" in d
        assert "SecurityTypedDict" in d

    def test_security_model_instantiation(self):
        from griddy.pfr.models.entities.security import Security

        sec = Security(pfr_auth="test_token")
        assert sec.pfr_auth == "test_token"
