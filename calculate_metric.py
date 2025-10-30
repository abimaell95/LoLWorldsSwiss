def calculate_metric(worlds_df):
    import pandas as pd

    all_teams = pd.unique(list(worlds_df['Team 1'].unique()) + list(worlds_df['Team 2'].unique()))
    scores_main = {team: 0 for team in all_teams}
    scores_metric = {team: 0 for team in all_teams}
    max_round = int(worlds_df['Round'].max())
    opponent_history = {team: [] for team in all_teams}
    round_cols = [f'Ronda{r}' for r in range(1, max_round + 1)]
    final_df = pd.DataFrame(index=all_teams, columns=round_cols + ['Score (métrica)', 'Score (Normal)'])
    final_df = final_df.fillna(0)
    
    for current_round in range(1, max_round + 1):
        matches_in_round = worlds_df[worlds_df['Round'] == current_round]
        for _, row in matches_in_round.iterrows():
            winner = row['WIN']
            loser = row['Team 2'] if winner == row['Team 1'] else row['Team 1']
            
            # Score normal
            scores_main[winner] += 1
            scores_main[loser] -= 1
            # Score métrica directo
            scores_metric[winner] += 1
            scores_metric[loser] -= 1
            
            # Ajustes colindantes: el resultado ACTUAL de 'winner' afecta a sus antiguos oponentes
            for opp_team, opp_round_played, team_past_result in opponent_history[winner]:
                # team_past_result es el resultado del 'winner' en ese pasado partido.
                # Si team_past_result == 'WIN' => el antiguo oponente perdió entonces (no ajustar ahora si winner gana).
                if team_past_result == 'LOSE':
                    # El antiguo oponente había ganado en ese enfrentamiento; ahora su ex-oponente (winner) gana -> +1
                    scores_metric[opp_team] += 1
            
            # Ajustes colindantes: el resultado ACTUAL de 'loser' afecta a sus antiguos oponentes
            for opp_team, opp_round_played, team_past_result in opponent_history[loser]:
                # Si team_past_result == 'WIN' => el loser ganó en aquel partido; ahora pierde -> antiguo oponente -1
                if team_past_result == 'WIN':
                    scores_metric[opp_team] -= 1
            
            # Registrar en historial
            opponent_history[winner].append((loser, current_round, 'WIN'))
            opponent_history[loser].append((winner, current_round, 'LOSE'))
        
        # Guardar acumulado al final de la ronda
        for team in all_teams:
            final_df.loc[team, f'Ronda{current_round}'] = scores_metric[team]
    
    # Llenar scores finales
    for team in all_teams:
        final_df.loc[team, 'Score (métrica)'] = scores_metric[team]
        final_df.loc[team, 'Score (Normal)'] = scores_main[team]
    
    final_df = final_df.sort_values(by='Score (métrica)', ascending=False).reset_index().rename(columns={'index':'Team'})
    return final_df
