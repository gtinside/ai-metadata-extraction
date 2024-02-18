import instructor
from pydantic import BaseModel

class Metadata(BaseModel):
    def __str__(self):
        return f"Metadata(\n" \
               f"    year={self.year},\n" \
               f"    quarter={self.quarter},\n" \
               f"    dap_in_billions={self.dap_in_billions},\n" \
               f"    map_in_billions={self.map_in_billions},\n" \
               f"    dau_in_billions={self.dau_in_billions},\n" \
               f"    mau_in_billions={self.mau_in_billions},\n" \
               f"    ad_impressions_change_quater={self.ad_impressions_change_quater},\n" \
               f"    ad_impressions_change_year={self.ad_impressions_change_year},\n" \
               f"    price_per_ad_change_quater={self.price_per_ad_change_quater},\n" \
               f"    price_per_ad_change_year={self.price_per_ad_change_year},\n" \
               f"    revenue_quarter_in_billions={self.revenue_quarter_in_billions},\n" \
               f"    revenue_change_quarter={self.revenue_change_quarter},\n" \
               f"    revenue_year_in_billions={self.revenue_year_in_billions},\n" \
               f"    revenue_change_year={self.revenue_change_year},\n" \
               f"    costs_in_billions={self.costs_in_billions},\n" \
               f"    expenses_in_billions={self.expenses_in_billions},\n" \
               f"    capital_expenditures_quarter_in_billions={self.capital_expenditures_quarter_in_billions},\n" \
               f"    capital_expenditures_year_in_billions={self.capital_expenditures_year_in_billions},\n" \
               f"    share_repurchases_quarter_in_billions={self.share_repurchases_quarter_in_billions},\n" \
               f"    share_repurchases_year_in_billions={self.share_repurchases_year_in_billions},\n" \
               f"    cash_in_billions={self.cash_in_billions},\n" \
               f"    free_cash_flow_quarter_in_billions={self.free_cash_flow_quarter_in_billions},\n" \
               f"    free_cash_flow_year_in_billions={self.free_cash_flow_year_in_billions},\n" \
               f"    long_term_debt_in_billions={self.long_term_debt_in_billions},\n" \
               f"    headcount={self.headcount},\n" \
               f"    headcount_change={self.headcount_change}\n" \
               f")"
    year: int
    quarter: str
    dap_in_billions: float
    map_in_billions: float
    dau_in_billions: float
    mau_in_billions: float
    ad_impressions_change_quater: float
    ad_impressions_change_year: float
    price_per_ad_change_quater: float
    price_per_ad_change_year: float
    revenue_quarter_in_billions: float
    revenue_change_quarter: float
    revenue_year_in_billions: float
    revenue_change_year: float
    costs_in_billions: float
    expenses_in_billions: float
    capital_expenditures_quarter_in_billions: float
    capital_expenditures_year_in_billions: float
    share_repurchases_quarter_in_billions: float
    share_repurchases_year_in_billions: float
    cash_in_billions: float
    free_cash_flow_quarter_in_billions:float
    free_cash_flow_year_in_billions: float
    long_term_debt_in_billions: float
    headcount: int
    headcount_change: float    

MayBeMetadata = instructor.Maybe(Metadata)