# tests/test_data.py

import unittest
import pandas as pd
from scripts.data_processing import load_data, clean_data, preprocess_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures, if any."""
        self.file_path = 'data/processed/solar_data.csv'
        self.df = pd.DataFrame({
            'Timestamp': ['2024-08-01 00:00:00', '2024-08-01 01:00:00', '2024-08-01 02:00:00'],
            'GHI': [100, 200, 300],
            'DNI': [50, 100, 150]
        })

    def test_load_data(self):
        """Test loading data from CSV."""
        df_loaded = load_data(self.file_path)
        self.assertIsNotNone(df_loaded)

    def test_clean_data(self):
        """Test data cleaning by removing missing values and duplicates."""
        df_cleaned = clean_data(self.df)
        self.assertEqual(df_cleaned.shape[0], 3)

    def test_preprocess_data(self):
        """Test data preprocessing like converting data types."""
        df_cleaned = clean_data(self.df)
        df_preprocessed = preprocess_data(df_cleaned)
        self.assertEqual(df_preprocessed['Timestamp'].dtype, '<M8[ns]')