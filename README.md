# ai-metadata-extraction
Code that converts the strings from META's earnings press release into a standardized type

### Dependencies
- [instructor](https://github.com/jxnl/instructor): Structured outputs powered by LLMs
- OPENAI_API_KEY: Environment variable
- Earnings file: ```earnings/earnings.json```

### How to ?
- Use this utility: ```python main.py```

### Sample Output
```
Metadata(
    year=2023,
    quarter=Q4,
    dap_in_billions=3.19,
    map_in_billions=3.98,
    dau_in_billions=2.11,
    mau_in_billions=3.07,
    ad_impressions_change_quater=21.0,
    ad_impressions_change_year=28.0,
    price_per_ad_change_quater=2.0,
    price_per_ad_change_year=-9.0,
    revenue_quarter_in_billions=40.11,
    revenue_change_quarter=25.0,
    revenue_year_in_billions=134.9,
    revenue_change_year=16.0,
    costs_in_billions=23.73,
    expenses_in_billions=88.15,
    capital_expenditures_quarter_in_billions=7.9,
    capital_expenditures_year_in_billions=28.1,
    share_repurchases_quarter_in_billions=6.32,
    share_repurchases_year_in_billions=20.03,
    cash_in_billions=65.4,
    free_cash_flow_quarter_in_billions=11.5,
    free_cash_flow_year_in_billions=43.01,
    long_term_debt_in_billions=18.39,
    headcount=67317,
    headcount_change=-22.0
)
```

### Working
Instructor leverages Pydantic to do heavy lifting. Refer to ```assets/metadata.py``` for the model class. Instructor provides API to convert unstructured data into structured format.
