import pandas as pd

def count_streak(df: pd.DataFrame):

    user_days = df.groupby('UserID')['Days']
    streaks = {user:1 for user in user_days.indices}

    for user, days in user_days:
        days_list = days.to_list()

        for i in range(1, len(days_list)):
            if int(days_list[i]) == int(days_list[i-1]) + 1:
                streaks[user] += 1

    return streaks

df = pd.DataFrame({
    "UserID": [
        "A", "A", "A", "A",
        "B", "B", "B",
        "C", "C"
    ],
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-05",

        "2026-01-10",
        "2026-01-12",
        "2026-01-13",

        "2026-01-20",
        "2026-01-21"
    ]
})

def main():
    # For simplicty, extract days, although this is the same method with months involved as well
    days = [d for d in df["Date"]]
    user_days = [d.split('-')[2] for d in days]

    df["Days"] = user_days
    
    print(df.head(20))
    print()

    print(count_streak(df))

main()