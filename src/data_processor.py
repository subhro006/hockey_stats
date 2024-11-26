import xlsxwriter
from typing import List, Dict

def process_hockey_data(stats: List[Dict[str, str]]) -> Dict[str, List]:
    # Organize stats by year
    stats_by_year = {}
    for stat in stats:
        year = stat["year"]
        if year not in stats_by_year:
            stats_by_year[year] = []
        stats_by_year[year].append(stat)
    
    # Generate winner/loser summary
    summary = []
    for year, teams in stats_by_year.items():
        winner = max(teams, key=lambda t: t["wins"])
        loser = min(teams, key=lambda t: t["wins"])
        summary.append({
            "year": year,
            "winner": winner["team"],
            "winner_wins": winner["wins"],
            "loser": loser["team"],
            "loser_wins": loser["wins"],
        })

    return {"stats": stats, "summary": summary}

def save_to_excel(html_files: List[str], excel_data: Dict[str, List]):
    # Create Excel Workbook
    workbook = xlsxwriter.Workbook("hockey_stats.xlsx")
    
    # Sheet 1: NHL Stats
    sheet1 = workbook.add_worksheet("NHL Stats 1990-2011")
    sheet1.write_row(0, 0, ["Year", "Team", "Wins", "Losses"])
    for row_idx, stat in enumerate(excel_data["stats"], 1):
        sheet1.write_row(row_idx, 0, [stat["year"], stat["team"], stat["wins"], stat["losses"]])
    
    # Sheet 2: Winner and Loser per Year
    sheet2 = workbook.add_worksheet("Winner and Loser per Year")
    sheet2.write_row(0, 0, ["Year", "Winner", "Winner Wins", "Loser", "Loser Wins"])
    for row_idx, summary in enumerate(excel_data["summary"], 1):
        sheet2.write_row(row_idx, 0, [
            summary["year"], 
            summary["winner"], 
            summary["winner_wins"], 
            summary["loser"], 
            summary["loser_wins"],
        ])
    
    workbook.close()
