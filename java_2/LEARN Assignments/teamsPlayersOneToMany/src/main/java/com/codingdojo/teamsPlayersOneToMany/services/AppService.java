package com.codingdojo.teamsPlayersOneToMany.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.codingdojo.teamsPlayersOneToMany.models.Team;
import com.codingdojo.teamsPlayersOneToMany.repositories.PlayerRepository;
import com.codingdojo.teamsPlayersOneToMany.repositories.TeamRepository;

@Service
public class AppService {
	
//tell service about the repositories.
	
	private final TeamRepository teamRepo;
	
	private final PlayerRepository playerRepo;
	
	public AppService(TeamRepository teamRepo, PlayerRepository playerRepo) {
		this.teamRepo = teamRepo;
		this.playerRepo = playerRepo;
	}
	
//	GET all teams.
	
	public List<Team> findAllTeams() {
		return (List<Team>)this.teamRepo.findAll();
	}
	
//	CREATE a team.
	
	public Team createTeam(Team t) {
		return this.teamRepo.save(t);
	}
	
	
	
	
	
	
	
	
}
