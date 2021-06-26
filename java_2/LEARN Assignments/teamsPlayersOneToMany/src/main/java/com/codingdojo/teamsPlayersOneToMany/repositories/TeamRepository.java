package com.codingdojo.teamsPlayersOneToMany.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.teamsPlayersOneToMany.models.Team;

@Repository
public interface TeamRepository extends CrudRepository<Team, Long>{

}
