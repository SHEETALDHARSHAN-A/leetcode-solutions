import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uni = employee["salary"].drop_duplicates()
    sec_high = uni.nlargest(2).iloc[-1] if len(uni)>=2 else None

    if sec_high is None:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    result_df = pd.DataFrame({'SecondHighestSalary' : [sec_high]})

    return result_df
