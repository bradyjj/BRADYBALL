from src.common.pydantic_models import *

# Soccerdata Leagues
BIG_5_EUROPEAN_LEAGUES_COMBINED = 'Big 5 European Leagues Combined'
ENG_PREMIER_LEAGUE = 'ENG-Premier League'
ESP_LA_LIGA = 'ESP-La Liga'
FRA_LIGUE_1 = 'FRA-Ligue 1'
GER_BUNDESLIGA = 'GER-Bundesliga'
ITA_SERIE_A = 'ITA-Serie A'

SOCCERDATA_LEAGUES = [
    # BIG_5_EUROPEAN_LEAGUES_COMBINED,
    # ENG_PREMIER_LEAGUE,
    # ESP_LA_LIGA,
    FRA_LIGUE_1,
    # GER_BUNDESLIGA,
    # ITA_SERIE_A
]

# FBREF
FBREF_STAT_CATEGORIES = [
    'standard',
    'keeper',
    'keeper_adv',
    'shooting',
    'passing',
    'passing_types',
    'goal_shot_creation',
    'defense',
    'possession',
    'playing_time',
    'misc'
]

FBREF_STAT_CATEGORY_TEAM_MODELS = {
    'standard': FbrTmStandardStats,
    'keeper': FbrTmKeeperStats,
    'keeper_adv': FbrTmKeeperAdvStats,
    'shooting': FbrTmShootingStats,
    'passing': FbrTmPassingStats,
    'passing_types': FbrTmPassingTypesStats,
    'goal_shot_creation': FbrTmGoalShotCreationStats,
    'defense': FbrTmDefenseStats,
    'possession': FbrTmPossessionStats,
    'playing_time': FbrTmPlayingTimeStats,
    'misc': FbrTmMiscStats
}

FBR_TM_STANDARD_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('Age', ''): 'average_age',
    ('Poss', ''): 'possession_pct',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Starts'): 'playing_time_starts',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', '90s'): 'playing_time_90s',
    ('Performance', 'Gls'): 'performance_gls',
    ('Performance', 'Ast'): 'performance_ast',
    ('Performance', 'G+A'): 'performance_g_a',
    ('Performance', 'G-PK'): 'performance_g_pk',
    ('Performance', 'PK'): 'performance_pk',
    ('Performance', 'PKatt'): 'performance_pkatt',
    ('Performance', 'CrdY'): 'performance_crd_y',
    ('Performance', 'CrdR'): 'performance_crd_r',
    ('Expected', 'xG'): 'expected_xg',
    ('Expected', 'npxG'): 'expected_npxg',
    ('Expected', 'xAG'): 'expected_xag',
    ('Expected', 'npxG+xAG'): 'expected_npxg_xag',
    ('Progression', 'PrgC'): 'progression_prgc',
    ('Progression', 'PrgP'): 'progression_prgp',
    ('Per 90 Minutes', 'Gls'): 'per_90_minutes_gls',
    ('Per 90 Minutes', 'Ast'): 'per_90_minutes_ast',
    ('Per 90 Minutes', 'G+A'): 'per_90_minutes_g_a',
    ('Per 90 Minutes', 'G-PK'): 'per_90_minutes_g_pk',
    ('Per 90 Minutes', 'G+A-PK'): 'per_90_minutes_g_a_pk',
    ('Per 90 Minutes', 'xG'): 'per_90_minutes_xg',
    ('Per 90 Minutes', 'xAG'): 'per_90_minutes_xag',
    ('Per 90 Minutes', 'xG+xAG'): 'per_90_minutes_xg_xag',
    ('Per 90 Minutes', 'npxG'): 'per_90_minutes_npxg',
    ('Per 90 Minutes', 'npxG+xAG'): 'per_90_minutes_npxg_xag',
    ('url', ''): 'url'
}

FBR_TM_DEFENSE_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Tackles', 'Tkl'): 'tackles_tkl',
    ('Tackles', 'TklW'): 'tackles_tklw',
    ('Tackles', 'Def 3rd'): 'tackles_def_3rd',
    ('Tackles', 'Mid 3rd'): 'tackles_mid_3rd',
    ('Tackles', 'Att 3rd'): 'tackles_att_3rd',
    ('Challenges', 'Tkl'): 'challenges_tkl',
    ('Challenges', 'Att'): 'challenges_att',
    ('Challenges', 'Tkl%'): 'challenges_tkl_pct',
    ('Challenges', 'Lost'): 'challenges_lost',
    ('Blocks', 'Blocks'): 'blocks_blocks',
    ('Blocks', 'Sh'): 'blocks_sh',
    ('Blocks', 'Pass'): 'blocks_pass',
    ('Int', ''): 'interceptions',
    ('Tkl+Int', ''): 'tackles_plus_interceptions',
    ('Clr', ''): 'clearances',
    ('Err', ''): 'errors',
    ('url', ''): 'url'
}

FBR_TM_GOAL_SHOT_CREATION_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('SCA', 'SCA'): 'sca_total',
    ('SCA', 'SCA90'): 'sca_per_90',
    ('SCA Types', 'PassLive'): 'sca_types_pass_live',
    ('SCA Types', 'PassDead'): 'sca_types_pass_dead',
    ('SCA Types', 'TO'): 'sca_types_to',
    ('SCA Types', 'Sh'): 'sca_types_sh',
    ('SCA Types', 'Fld'): 'sca_types_fld',
    ('SCA Types', 'Def'): 'sca_types_def',
    ('GCA', 'GCA'): 'gca_total',
    ('GCA', 'GCA90'): 'gca_per_90',
    ('GCA Types', 'PassLive'): 'gca_types_pass_live',
    ('GCA Types', 'PassDead'): 'gca_types_pass_dead',
    ('GCA Types', 'TO'): 'gca_types_to',
    ('GCA Types', 'Sh'): 'gca_types_sh',
    ('GCA Types', 'Fld'): 'gca_types_fld',
    ('GCA Types', 'Def'): 'gca_types_def',
    ('url', ''): 'url'
}

FBR_TM_KEEPER_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Starts'): 'playing_time_starts',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', '90s'): 'playing_time_90s',
    ('Performance', 'GA'): 'performance_ga',
    ('Performance', 'GA90'): 'performance_ga90',
    ('Performance', 'SoTA'): 'performance_sota',
    ('Performance', 'Saves'): 'performance_saves',
    ('Performance', 'Save%'): 'performance_save_pct',
    ('Performance', 'W'): 'performance_w',
    ('Performance', 'D'): 'performance_d',
    ('Performance', 'L'): 'performance_l',
    ('Performance', 'CS'): 'performance_cs',
    ('Performance', 'CS%'): 'performance_cs_pct',
    ('Penalty Kicks', 'PKatt'): 'penalty_kicks_pkatt',
    ('Penalty Kicks', 'PKA'): 'penalty_kicks_pka',
    ('Penalty Kicks', 'PKsv'): 'penalty_kicks_pksv',
    ('Penalty Kicks', 'PKm'): 'penalty_kicks_pkm',
    ('Penalty Kicks', 'Save%'): 'penalty_kicks_save_pct',
    ('url', ''): 'url'
}

FBR_TM_KEEPER_ADV_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Goals', 'GA'): 'goals_ga',
    ('Goals', 'PKA'): 'goals_pka',
    ('Goals', 'FK'): 'goals_fk',
    ('Goals', 'CK'): 'goals_ck',
    ('Goals', 'OG'): 'goals_og',
    ('Expected', 'PSxG'): 'expected_psxg',
    ('Expected', 'PSxG/SoT'): 'expected_psxg_sot',
    ('Expected', 'PSxG+/-'): 'expected_psxg_plus_minus',
    ('Expected', '/90'): 'expected_per_90',
    ('Launched', 'Cmp'): 'launched_cmp',
    ('Launched', 'Att'): 'launched_att',
    ('Launched', 'Cmp%'): 'launched_cmp_pct',
    ('Passes', 'Att (GK)'): 'passes_att_gk',
    ('Passes', 'Thr'): 'passes_thr',
    ('Passes', 'Launch%'): 'passes_launch_pct',
    ('Passes', 'AvgLen'): 'passes_avg_len',
    ('Goal Kicks', 'Att'): 'goal_kicks_att',
    ('Goal Kicks', 'Launch%'): 'goal_kicks_launch_pct',
    ('Goal Kicks', 'AvgLen'): 'goal_kicks_avg_len',
    ('Crosses', 'Opp'): 'crosses_opp',
    ('Crosses', 'Stp'): 'crosses_stp',
    ('Crosses', 'Stp%'): 'crosses_stp_pct',
    ('Sweeper', '#OPA'): 'sweeper_opa',
    ('Sweeper', '#OPA/90'): 'sweeper_opa_per_90',
    ('Sweeper', 'AvgDist'): 'sweeper_avg_dist',
    ('url', ''): 'url'
}

FBR_TM_MISC_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Performance', 'CrdY'): 'performance_crdy',
    ('Performance', 'CrdR'): 'performance_crdr',
    ('Performance', '2CrdY'): 'performance_2crdy',
    ('Performance', 'Fls'): 'performance_fls',
    ('Performance', 'Fld'): 'performance_fld',
    ('Performance', 'Off'): 'performance_off',
    ('Performance', 'Crs'): 'performance_crs',
    ('Performance', 'Int'): 'performance_int',
    ('Performance', 'TklW'): 'performance_tklw',
    ('Performance', 'PKwon'): 'performance_pkwon',
    ('Performance', 'PKcon'): 'performance_pkcon',
    ('Performance', 'OG'): 'performance_og',
    ('Performance', 'Recov'): 'performance_recov',
    ('Aerial Duels', 'Won'): 'aerial_duels_won',
    ('Aerial Duels', 'Lost'): 'aerial_duels_lost',
    ('Aerial Duels', 'Won%'): 'aerial_duels_won_pct',
    ('url', ''): 'url'
}

FBR_TM_PASSING_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Total', 'Cmp'): 'total_cmp',
    ('Total', 'Att'): 'total_att',
    ('Total', 'Cmp%'): 'total_cmp_pct',
    ('Total', 'TotDist'): 'total_tot_dist',
    ('Total', 'PrgDist'): 'total_prg_dist',
    ('Short', 'Cmp'): 'short_cmp',
    ('Short', 'Att'): 'short_att',
    ('Short', 'Cmp%'): 'short_cmp_pct',
    ('Medium', 'Cmp'): 'medium_cmp',
    ('Medium', 'Att'): 'medium_att',
    ('Medium', 'Cmp%'): 'medium_cmp_pct',
    ('Long', 'Cmp'): 'long_cmp',
    ('Long', 'Att'): 'long_att',
    ('Long', 'Cmp%'): 'long_cmp_pct',
    ('Ast', ''): 'ast',
    ('xAG', ''): 'xag',
    ('Expected', 'xA'): 'expected_xa',
    ('Expected', 'A-xAG'): 'expected_a_xag',
    ('KP', ''): 'kp',
    ('1/3', ''): 'passes_into_final_third',
    ('PPA', ''): 'ppa',
    ('CrsPA', ''): 'crspa',
    ('PrgP', ''): 'prog_passes',
    ('url', ''): 'url'
}

FBR_TM_PASSING_TYPES_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Att', ''): 'total_att',
    ('Pass Types', 'Live'): 'pass_types_live',
    ('Pass Types', 'Dead'): 'pass_types_dead',
    ('Pass Types', 'FK'): 'pass_types_fk',
    ('Pass Types', 'TB'): 'pass_types_tb',
    ('Pass Types', 'Sw'): 'pass_types_sw',
    ('Pass Types', 'Crs'): 'pass_types_crs',
    ('Pass Types', 'TI'): 'pass_types_ti',
    ('Pass Types', 'CK'): 'pass_types_ck',
    ('Corner Kicks', 'In'): 'corner_kicks_in',
    ('Corner Kicks', 'Out'): 'corner_kicks_out',
    ('Corner Kicks', 'Str'): 'corner_kicks_str',
    ('Outcomes', 'Cmp'): 'outcomes_cmp',
    ('Outcomes', 'Off'): 'outcomes_off',
    ('Outcomes', 'Blocks'): 'outcomes_blocks',
    ('url', ''): 'url'
}

FBR_TM_PLAYING_TIME_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('Age', ''): 'average_age',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', 'Mn/MP'): 'playing_time_mn_per_mp',
    ('Playing Time', 'Min%'): 'playing_time_min_pct',
    ('Playing Time', '90s'): 'playing_time_90s',
    ('Starts', 'Starts'): 'starts_starts',
    ('Starts', 'Mn/Start'): 'starts_mn_per_start',
    ('Starts', 'Compl'): 'starts_compl',
    ('Subs', 'Subs'): 'subs_subs',
    ('Subs', 'Mn/Sub'): 'subs_mn_per_sub',
    ('Subs', 'unSub'): 'subs_unsub',
    ('Team Success', 'PPM'): 'team_success_ppm',
    ('Team Success', 'onG'): 'team_success_ong',
    ('Team Success', 'onGA'): 'team_success_onga',
    ('Team Success', '+/-'): 'team_success_plus_minus',
    ('Team Success', '+/-90'): 'team_success_plus_minus_per_90',
    ('Team Success (xG)', 'onxG'): 'team_success_xg_ongxg',
    ('Team Success (xG)', 'onxGA'): 'team_success_xg_ongxga',
    ('Team Success (xG)', 'xG+/-'): 'team_success_xg_xg_plus_minus',
    ('Team Success (xG)', 'xG+/-90'): 'team_success_xg_xg_plus_minus_per_90',
    ('url', ''): 'url'
}

FBR_TM_POSSESSION_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('Poss', ''): 'possession_pct',
    ('90s', ''): 'minutes_90s',
    ('Touches', 'Touches'): 'touches_total',
    ('Touches', 'Def Pen'): 'touches_def_pen',
    ('Touches', 'Def 3rd'): 'touches_def_3rd',
    ('Touches', 'Mid 3rd'): 'touches_mid_3rd',
    ('Touches', 'Att 3rd'): 'touches_att_3rd',
    ('Touches', 'Att Pen'): 'touches_att_pen',
    ('Touches', 'Live'): 'touches_live',
    ('Take-Ons', 'Att'): 'take_ons_att',
    ('Take-Ons', 'Succ'): 'take_ons_succ',
    ('Take-Ons', 'Succ%'): 'take_ons_succ_pct',
    ('Take-Ons', 'Tkld'): 'take_ons_tkld',
    ('Take-Ons', 'Tkld%'): 'take_ons_tkld_pct',
    ('Carries', 'Carries'): 'carries_total',
    ('Carries', 'TotDist'): 'carries_tot_dist',
    ('Carries', 'PrgDist'): 'carries_prg_dist',
    ('Carries', 'PrgC'): 'carries_prgc',
    ('Carries', '1/3'): 'carries_1_3',
    ('Carries', 'CPA'): 'carries_cpa',
    ('Carries', 'Mis'): 'carries_mis',
    ('Carries', 'Dis'): 'carries_dis',
    ('Receiving', 'Rec'): 'receiving_rec',
    ('Receiving', 'PrgR'): 'receiving_prg_r',
    ('url', ''): 'url'
}

FBR_TM_SHOOTING_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('players_used', ''): 'players_used',
    ('90s', ''): 'minutes_90s',
    ('Standard', 'Gls'): 'standard_gls',
    ('Standard', 'Sh'): 'standard_sh',
    ('Standard', 'SoT'): 'standard_sot',
    ('Standard', 'SoT%'): 'standard_sot_pct',
    ('Standard', 'Sh/90'): 'standard_sh_per_90',
    ('Standard', 'SoT/90'): 'standard_sot_per_90',
    ('Standard', 'G/Sh'): 'standard_g_sh',
    ('Standard', 'G/SoT'): 'standard_g_sot',
    ('Standard', 'Dist'): 'standard_dist',
    ('Standard', 'FK'): 'standard_fk',
    ('Standard', 'PK'): 'standard_pk',
    ('Standard', 'PKatt'): 'standard_pkatt',
    ('Expected', 'xG'): 'expected_xg',
    ('Expected', 'npxG'): 'expected_npxg',
    ('Expected', 'npxG/Sh'): 'expected_npxg_per_sh',
    ('Expected', 'G-xG'): 'expected_g_xg',
    ('Expected', 'np:G-xG'): 'expected_np_g_xg',
    ('url', ''): 'url'
}

FBREF_TEAM_MODELS_MAPPINGS = {
    FbrTmDefenseStats: FBR_TM_DEFENSE_STATS_MAPPINGS,
    FbrTmGoalShotCreationStats: FBR_TM_GOAL_SHOT_CREATION_STATS_MAPPINGS,
    FbrTmKeeperAdvStats: FBR_TM_KEEPER_ADV_STATS_MAPPINGS,
    FbrTmKeeperStats: FBR_TM_KEEPER_STATS_MAPPINGS,
    FbrTmMiscStats: FBR_TM_MISC_STATS_MAPPINGS,
    FbrTmPassingStats: FBR_TM_PASSING_STATS_MAPPINGS,
    FbrTmPassingTypesStats: FBR_TM_PASSING_TYPES_STATS_MAPPINGS,
    FbrTmPlayingTimeStats: FBR_TM_PLAYING_TIME_STATS_MAPPINGS,
    FbrTmPossessionStats: FBR_TM_POSSESSION_STATS_MAPPINGS,
    FbrTmShootingStats: FBR_TM_SHOOTING_STATS_MAPPINGS,
    FbrTmStandardStats: FBR_TM_STANDARD_STATS_MAPPINGS,
}

# Create a dictionary to map each team stat category to its corresponding table name
STAT_CATEGORY_TEAM_TABLE_NAMES = {
    stat_category: f"fbr_tm_{stat_category.lower()}_stats"
    for stat_category in FBREF_STAT_CATEGORY_TEAM_MODELS
}

FBREF_STAT_CATEGORY_PLAYER_MODELS = {
    'standard': FbrPlStandardStats,
    'keeper': FbrPlKeeperStats,
    'keeper_adv': FbrPlKeeperAdvStats,
    'shooting': FbrPlShootingStats,
    'passing': FbrPlPassingStats,
    'passing_types': FbrPlPassingTypesStats,
    'goal_shot_creation': FbrPlGoalShotCreationStats,
    'defense': FbrPlDefenseStats,
    'possession': FbrPlPossessionStats,
    'playing_time': FbrPlPlayingTimeStats,
    'misc': FbrPlMiscStats
}

FBR_PL_STANDARD_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Starts'): 'playing_time_starts',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', '90s'): 'playing_time_90s',
    ('Performance', 'Gls'): 'performance_gls',
    ('Performance', 'Ast'): 'performance_ast',
    ('Performance', 'G+A'): 'performance_g_a',
    ('Performance', 'G-PK'): 'performance_g_pk',
    ('Performance', 'PK'): 'performance_pk',
    ('Performance', 'PKatt'): 'performance_pkatt',
    ('Performance', 'CrdY'): 'performance_crd_y',
    ('Performance', 'CrdR'): 'performance_crd_r',
    ('Expected', 'xG'): 'expected_xg',
    ('Expected', 'npxG'): 'expected_npxg',
    ('Expected', 'xAG'): 'expected_xag',
    ('Expected', 'npxG+xAG'): 'expected_npxg_xag',
    ('Progression', 'PrgC'): 'progression_prgc',
    ('Progression', 'PrgP'): 'progression_prgp',
    ('Progression', 'PrgR'): 'progression_prgr',
    ('Per 90 Minutes', 'Gls'): 'p90_gls',
    ('Per 90 Minutes', 'Ast'): 'p90_ast',
    ('Per 90 Minutes', 'G+A'): 'p90_g_a',
    ('Per 90 Minutes', 'G-PK'): 'p90_g_pk',
    ('Per 90 Minutes', 'G+A-PK'): 'p90_g_a_pk',
    ('Per 90 Minutes', 'xG'): 'p90_xg',
    ('Per 90 Minutes', 'xAG'): 'p90_xag',
    ('Per 90 Minutes', 'xG+xAG'): 'p90_xg_xag',
    ('Per 90 Minutes', 'npxG'): 'p90_npxg',
    ('Per 90 Minutes', 'npxG+xAG'): 'p90_npxg_xag',
}

FBR_PL_KEEPER_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Starts'): 'playing_time_starts',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', '90s'): 'playing_time_90s',
    ('Performance', 'GA'): 'performance_ga',
    ('Performance', 'GA90'): 'performance_ga90',
    ('Performance', 'SoTA'): 'performance_sota',
    ('Performance', 'Saves'): 'performance_saves',
    ('Performance', 'Save%'): 'performance_save_pct',
    ('Performance', 'W'): 'performance_w',
    ('Performance', 'D'): 'performance_d',
    ('Performance', 'L'): 'performance_l',
    ('Performance', 'CS'): 'performance_cs',
    ('Performance', 'CS%'): 'performance_cs_pct',
    ('Penalty Kicks', 'PKatt'): 'penalty_kicks_pkatt',
    ('Penalty Kicks', 'PKA'): 'penalty_kicks_pka',
    ('Penalty Kicks', 'PKsv'): 'penalty_kicks_pksv',
    ('Penalty Kicks', 'PKm'): 'penalty_kicks_pkm',
    ('Penalty Kicks', 'Save%'): 'penalty_kicks_save_pct',
}

FBR_PL_KEEPER_ADV_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Goals', 'GA'): 'goals_ga',
    ('Goals', 'PKA'): 'goals_pka',
    ('Goals', 'FK'): 'goals_fk',
    ('Goals', 'CK'): 'goals_ck',
    ('Goals', 'OG'): 'goals_og',
    ('Expected', 'PSxG'): 'expected_psxg',
    ('Expected', 'PSxG/SoT'): 'expected_psxg_sot',
    ('Expected', 'PSxG+/-'): 'expected_psxg_plus_minus',
    ('Expected', '/90'): 'expected_per_90',
    ('Launched', 'Cmp'): 'launched_cmp',
    ('Launched', 'Att'): 'launched_att',
    ('Launched', 'Cmp%'): 'launched_cmp_pct',
    ('Passes', 'Att (GK)'): 'passes_att_gk',
    ('Passes', 'Thr'): 'passes_thr',
    ('Passes', 'Launch%'): 'passes_launch_pct',
    ('Passes', 'AvgLen'): 'passes_avg_len',
    ('Goal Kicks', 'Att'): 'goal_kicks_att',
    ('Goal Kicks', 'Launch%'): 'goal_kicks_launch_pct',
    ('Goal Kicks', 'AvgLen'): 'goal_kicks_avg_len',
    ('Crosses', 'Opp'): 'crosses_opp',
    ('Crosses', 'Stp'): 'crosses_stp',
    ('Crosses', 'Stp%'): 'crosses_stp_pct',
    ('Sweeper', '#OPA'): 'sweeper_opa',
    ('Sweeper', '#OPA/90'): 'sweeper_opa_per_90',
    ('Sweeper', 'AvgDist'): 'sweeper_avg_dist',
}

FBR_PL_SHOOTING_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Standard', 'Gls'): 'standard_gls',
    ('Standard', 'Sh'): 'standard_sh',
    ('Standard', 'SoT'): 'standard_sot',
    ('Standard', 'SoT%'): 'standard_sot_pct',
    ('Standard', 'Sh/90'): 'standard_sh_per_90',
    ('Standard', 'SoT/90'): 'standard_sot_per_90',
    ('Standard', 'G/Sh'): 'standard_g_sh',
    ('Standard', 'G/SoT'): 'standard_g_sot',
    ('Standard', 'Dist'): 'standard_dist',
    ('Standard', 'FK'): 'standard_fk',
    ('Standard', 'PK'): 'standard_pk',
    ('Standard', 'PKatt'): 'standard_pkatt',
    ('Expected', 'xG'): 'expected_xg',
    ('Expected', 'npxG'): 'expected_npxg',
    ('Expected', 'npxG/Sh'): 'expected_npxg_per_sh',
    ('Expected', 'G-xG'): 'expected_g_xg',
    ('Expected', 'np:G-xG'): 'expected_np_g_xg',
}

FBR_PL_DEFENSE_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Tackles', 'Tkl'): 'tackles_tkl',
    ('Tackles', 'TklW'): 'tackles_tklw',
    ('Tackles', 'Def 3rd'): 'tackles_def_3rd',
    ('Tackles', 'Mid 3rd'): 'tackles_mid_3rd',
    ('Tackles', 'Att 3rd'): 'tackles_att_3rd',
    ('Challenges', 'Tkl'): 'challenges_tkl',
    ('Challenges', 'Att'): 'challenges_att',
    ('Challenges', 'Tkl%'): 'challenges_tkl_pct',
    ('Challenges', 'Lost'): 'challenges_lost',
    ('Blocks', 'Blocks'): 'blocks_blocks',
    ('Blocks', 'Sh'): 'blocks_sh',
    ('Blocks', 'Pass'): 'blocks_pass',
    ('Int', ): 'interceptions',
    ('Tkl+Int', ): 'tackles_plus_interceptions',
    ('Clr', ): 'clearances',
    ('Err', ): 'errors',
}

FBR_PL_GOAL_SHOT_CREATION_STATS_MAPPINGS = {
    ('league', ): 'league',
    ('season', ): 'season',
    ('team', ): 'team',
    ('player', ): 'player',
    ('nation', ): 'nation',
    ('pos', ): 'pos',
    ('age', ): 'age',
    ('born', ): 'born',
    ('90s', ''): 'minutes_90s',
    ('SCA', 'SCA'): 'sca_total',
    ('SCA', 'SCA90'): 'sca_per_90',
    ('SCA Types', 'PassLive'): 'sca_types_pass_live',
    ('SCA Types', 'PassDead'): 'sca_types_pass_dead',
    ('SCA Types', 'TO'): 'sca_types_to',
    ('SCA Types', 'Sh'): 'sca_types_sh',
    ('SCA Types', 'Fld'): 'sca_types_fld',
    ('SCA Types', 'Def'): 'sca_types_def',
    ('GCA', 'GCA'): 'gca_total',
    ('GCA', 'GCA90'): 'gca_per_90',
    ('GCA Types', 'PassLive'): 'gca_types_pass_live',
    ('GCA Types', 'PassDead'): 'gca_types_pass_dead',
    ('GCA Types', 'TO'): 'gca_types_to',
    ('GCA Types', 'Sh'): 'gca_types_sh',
    ('GCA Types', 'Fld'): 'gca_types_fld',
    ('GCA Types', 'Def'): 'gca_types_def',
}

FBR_PL_MISC_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Performance', 'CrdY'): 'performance_crdy',
    ('Performance', 'CrdR'): 'performance_crdr',
    ('Performance', '2CrdY'): 'performance_2crdy',
    ('Performance', 'Fls'): 'performance_fls',
    ('Performance', 'Fld'): 'performance_fld',
    ('Performance', 'Off'): 'performance_off',
    ('Performance', 'Crs'): 'performance_crs',
    ('Performance', 'Int'): 'performance_int',
    ('Performance', 'TklW'): 'performance_tklw',
    ('Performance', 'PKwon'): 'performance_pkwon',
    ('Performance', 'PKcon'): 'performance_pkcon',
    ('Performance', 'OG'): 'performance_og',
    ('Performance', 'Recov'): 'performance_recov',
    ('Aerial Duels', 'Won'): 'aerial_duels_won',
    ('Aerial Duels', 'Lost'): 'aerial_duels_lost',
    ('Aerial Duels', 'Won%'): 'aerial_duels_won_pct',
}

FBR_PL_PASSING_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Total', 'Cmp'): 'total_cmp',
    ('Total', 'Att'): 'total_att',
    ('Total', 'Cmp%'): 'total_cmp_pct',
    ('Total', 'TotDist'): 'total_tot_dist',
    ('Total', 'PrgDist'): 'total_prg_dist',
    ('Short', 'Cmp'): 'short_cmp',
    ('Short', 'Att'): 'short_att',
    ('Short', 'Cmp%'): 'short_cmp_pct',
    ('Medium', 'Cmp'): 'medium_cmp',
    ('Medium', 'Att'): 'medium_att',
    ('Medium', 'Cmp%'): 'medium_cmp_pct',
    ('Long', 'Cmp'): 'long_cmp',
    ('Long', 'Att'): 'long_att',
    ('Long', 'Cmp%'): 'long_cmp_pct',
    ('Ast', ): 'ast',
    ('xAG', ): 'xag',
    ('Expected', 'xA'): 'expected_xa',
    ('Expected', 'A-xAG'): 'expected_a_xag',
    ('KP', ): 'kp',
    ('1/3', ): 'passes_into_final_third',
    ('PPA', ): 'ppa',
    ('CrsPA', ): 'crspa',
    ('PrgP', ): 'prog_passes',
}

FBR_PL_PASSING_TYPES_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Att', ''): 'att',
    ('Pass Types', 'Live'): 'pass_types_live',
    ('Pass Types', 'Dead'): 'pass_types_dead',
    ('Pass Types', 'FK'): 'pass_types_fk',
    ('Pass Types', 'TB'): 'pass_types_tb',
    ('Pass Types', 'Sw'): 'pass_types_sw',
    ('Pass Types', 'Crs'): 'pass_types_crs',
    ('Pass Types', 'TI'): 'pass_types_ti',
    ('Pass Types', 'CK'): 'pass_types_ck',
    ('Corner Kicks', 'In'): 'corner_kicks_in',
    ('Corner Kicks', 'Out'): 'corner_kicks_out',
    ('Corner Kicks', 'Str'): 'corner_kicks_str',
    ('Outcomes', 'Cmp'): 'outcomes_cmp',
    ('Outcomes', 'Off'): 'outcomes_off',
    ('Outcomes', 'Blocks'): 'outcomes_blocks',
}

FBR_PL_PLAYING_TIME_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('Playing Time', 'MP'): 'playing_time_mp',
    ('Playing Time', 'Min'): 'playing_time_min',
    ('Playing Time', 'Mn/MP'): 'playing_time_mn_per_mp',
    ('Playing Time', 'Min%'): 'playing_time_min_pct',
    ('Playing Time', '90s'): 'minutes_90s',
    ('Starts', 'Starts'): 'starts_starts',
    ('Starts', 'Mn/Start'): 'starts_mn_per_start',
    ('Starts', 'Compl'): 'starts_compl',
    ('Subs', 'Subs'): 'subs_subs',
    ('Subs', 'Mn/Sub'): 'subs_mn_per_sub',
    ('Subs', 'unSub'): 'subs_unsub',
    ('Team Success', 'PPM'): 'team_success_ppm',
    ('Team Success', 'onG'): 'team_success_ong',
    ('Team Success', 'onGA'): 'team_success_onga',
    ('Team Success', '+/-'): 'team_success_plus_minus',
    ('Team Success', '+/-90'): 'team_success_plus_minus_per_90',
    ('Team Success', 'On-Off'): 'team_success_on_off',
    ('Team Success (xG)', 'onxG'): 'team_success_xg_ongxg',
    ('Team Success (xG)', 'onxGA'): 'team_success_xg_ongxga',
    ('Team Success (xG)', 'xG+/-'): 'team_success_xg_plus_minus',
    ('Team Success (xG)', 'xG+/-90'): 'team_success_xg_plus_minus_per_90',
    ('Team Success (xG)', 'On-Off'): 'team_success_xg_on_off',
}

FBR_PL_POSSESSION_STATS_MAPPINGS = {
    ('league', ''): 'league',
    ('season', ''): 'season',
    ('team', ''): 'team',
    ('player', ''): 'player',
    ('nation', ''): 'nation',
    ('pos', ''): 'position',
    ('age', ''): 'age',
    ('born', ''): 'born',
    ('90s', ''): 'minutes_90s',
    ('Touches', 'Touches'): 'touches_total',
    ('Touches', 'Def Pen'): 'touches_def_pen',
    ('Touches', 'Def 3rd'): 'touches_def_3rd',
    ('Touches', 'Mid 3rd'): 'touches_mid_3rd',
    ('Touches', 'Att 3rd'): 'touches_att_3rd',
    ('Touches', 'Att Pen'): 'touches_att_pen',
    ('Touches', 'Live'): 'touches_live',
    ('Take-Ons', 'Att'): 'take_ons_att',
    ('Take-Ons', 'Succ'): 'take_ons_succ',
    ('Take-Ons', 'Succ%'): 'take_ons_succ_pct',
    ('Take-Ons', 'Tkld'): 'take_ons_tkld',
    ('Take-Ons', 'Tkld%'): 'take_ons_tkld_pct',
    ('Carries', 'Carries'): 'carries_total',
    ('Carries', 'TotDist'): 'carries_tot_dist',
    ('Carries', 'PrgDist'): 'carries_prg_dist',
    ('Carries', 'PrgC'): 'carries_prgc',
    ('Carries', '1/3'): 'carries_1_3',
    ('Carries', 'CPA'): 'carries_cpa',
    ('Carries', 'Mis'): 'carries_mis',
    ('Carries', 'Dis'): 'carries_dis',
    ('Receiving', 'Rec'): 'receiving_rec',
    ('Receiving', 'PrgR'): 'receiving_prg_r',
}

FBREF_PLAYER_MODELS_MAPPINGS = {
    FbrPlDefenseStats: FBR_PL_DEFENSE_STATS_MAPPINGS,
    FbrPlGoalShotCreationStats: FBR_PL_GOAL_SHOT_CREATION_STATS_MAPPINGS,
    FbrPlKeeperAdvStats: FBR_PL_KEEPER_ADV_STATS_MAPPINGS,
    FbrPlKeeperStats: FBR_PL_KEEPER_STATS_MAPPINGS,
    FbrPlMiscStats: FBR_PL_MISC_STATS_MAPPINGS,
    FbrPlPassingStats: FBR_PL_PASSING_STATS_MAPPINGS,
    FbrPlPassingTypesStats: FBR_PL_PASSING_TYPES_STATS_MAPPINGS,
    FbrPlPlayingTimeStats: FBR_PL_PLAYING_TIME_STATS_MAPPINGS,
    FbrPlPossessionStats: FBR_PL_POSSESSION_STATS_MAPPINGS,
    FbrPlShootingStats: FBR_PL_SHOOTING_STATS_MAPPINGS,
    FbrPlStandardStats: FBR_PL_STANDARD_STATS_MAPPINGS,
}

# Create a dictionary to map each player stat category to its corresponding table name
STAT_CATEGORY_PLAYER_TABLE_NAMES = {
    stat_category: f"fbr_pl_{stat_category.lower()}_stats"
    for stat_category in FBREF_STAT_CATEGORY_TEAM_MODELS
}

# WHOSCORED
WHOSCORED_URL = "https://www.whoscored.com"
WHOSCORED_MATCH_URL_TEMPLATE = "https://www.whoscored.com/Matches/{match_id}/{page}/{league}-{season}-{teams}"
WHOSCORED_URL_TO_CONST = {
    'England-Premier-League': ENG_PREMIER_LEAGUE,
    'Spain-LaLiga': ESP_LA_LIGA,
    'France-Ligue-1': FRA_LIGUE_1,
    'Germany-Bundesliga': GER_BUNDESLIGA,
    'Italy-Serie-A': ITA_SERIE_A
}

# TRANSFERMARKT
TRANSFERMARKT_PLAYER_URL = "https://www.transfermarkt.us/{player_name}/profil/spieler/{player_id}"
TRANSFERMARKT_TEAM_STAFF_URL = "https://www.transfermarkt.us/ceapi/staff/team/{team_id}/?saison_id={season_year}&wettbewerb_id={transfermarkt_league_id}"
TRANSFERMARKT_TRANSFER_HISTORY_URL = "https://www.transfermarkt.us/ceapi/transferHistory/list/{player_id}"
TRANSFERMARKT_MARKET_VALUE_URL = "https://www.transfermarkt.us/ceapi/marketValueDevelopment/graph/{player_id}"
TRANSFERMARKT_COUNTRY_URL = "https://www.transfermarkt.us/wettbewerbe/national/wettbewerbe/{country_id}/saison_id/{year}"
TRANSFERMARKT_COUNTRY_IDS = {
    "England": "189",
    "France": "50",
    "Spain": "157",
    "Germany": "40",
    "Italy": "75"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
