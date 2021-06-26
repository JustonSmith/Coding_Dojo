package com.codingdojo.teamsPlayersOneToMany.Controllers;

import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.codingdojo.teamsPlayersOneToMany.models.Team;
import com.codingdojo.teamsPlayersOneToMany.services.AppService;

@Controller
public class TeamController {
	
	private final AppService appService;
	
	public TeamController(AppService appService) {
		this.appService = appService;
	}
	
	@GetMapping("/")
	public String welcomeToTeam(Model model, @ModelAttribute("team") Team team)  {
		List<Team> allTeams = this.appService.findAllTeams();
		model.addAttribute("allTeams", allTeams);
		return "index.jsp";
	}
	
	@PostMapping("/teams/create")
	public String createNewTeam(@Valid @ModelAttribute("team") Team team, BindingResult result) {
		if(result.hasErrors()) {
			return "index.jsp";
		} else {
			this.appService.createTeam(team);
			return "redirect:/";
		}
	}
	
}
