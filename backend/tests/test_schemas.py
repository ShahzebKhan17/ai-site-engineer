import os
import sys
import uuid
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pydantic import ValidationError
from app.schemas.project import ProjectCreate
from app.schemas.calculation import RebarBarInput, RebarCalculationRequest, ConcreteCalculationRequest
from app.schemas.rag import RAGQueryRequest


class TestPydanticSchemas(unittest.TestCase):
    def test_project_create_schema_valid(self):
        proj = ProjectCreate(
            code="PRJ-METRO-01",
            name="Metro Viaduct Package 3",
            client="Delhi Metro Rail Corp",
            location="Sector 62, Noida",
            primary_standard="IS 456 / IS 1786",
        )
        self.assertEqual(proj.code, "PRJ-METRO-01")
        self.assertEqual(proj.name, "Metro Viaduct Package 3")

    def test_rebar_bar_input_schema_validation(self):
        # Valid input
        bar = RebarBarInput(
            bar_mark="B1",
            diameter_mm=25,
            length_m=3.8,
            number_of_bars=8,
            wastage_percent=3.5,
        )
        self.assertEqual(bar.diameter_mm, 25)
        self.assertEqual(bar.number_of_bars, 8)

        # Invalid diameter (> 50mm)
        with self.assertRaises(ValidationError):
            RebarBarInput(
                bar_mark="B2",
                diameter_mm=60,  # Invalid
                length_m=3.8,
                number_of_bars=8,
            )

        # Invalid negative count
        with self.assertRaises(ValidationError):
            RebarBarInput(
                bar_mark="B3",
                diameter_mm=16,
                length_m=3.8,
                number_of_bars=-1,  # Invalid
            )

    def test_rag_query_request_validation(self):
        query = RAGQueryRequest(
            project_id=uuid.uuid4(),
            query="What is the cover requirement for foundations in saline soil?",
            top_k=5,
        )
        self.assertEqual(query.top_k, 5)
        self.assertTrue(len(query.query) > 0)


if __name__ == "__main__":
    unittest.main()
