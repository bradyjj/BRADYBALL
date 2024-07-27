from fastapi import HTTPException
from src.api.services import database

async def get_player_data(player_name: str):
    tables = [
        "fbr_pl_standard_stats",
        "fbr_pl_shooting_stats",
        "fbr_pl_passing_stats",
        "fbr_pl_passing_types_stats",
        "fbr_pl_defense_stats",
        "fbr_pl_possession_stats",
        "fbr_pl_goal_shot_creation_stats",
        "fbr_pl_keeper_stats",
        "fbr_pl_keeper_adv_stats",
        "fbr_pl_playing_time_stats",
        "fbr_pl_misc_stats"
    ]
    
    results = {}
    for table in tables:
        data = await database.fetch_data(table, player_name)
        results[table] = data
    
    return results

async def combine_player_data(player_name: str, data: dict):
    combined_data = {}
    for dataset in data.values():
        for stat in dataset:
            season = stat['season']
            if season not in combined_data:
                combined_data[season] = {'season': season, 'player': player_name}
            combined_data[season].update(stat)
    
    return list(combined_data.values())