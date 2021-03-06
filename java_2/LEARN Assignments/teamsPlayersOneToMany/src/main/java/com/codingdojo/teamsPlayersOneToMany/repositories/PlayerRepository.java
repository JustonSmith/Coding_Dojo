package com.codingdojo.teamsPlayersOneToMany.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.teamsPlayersOneToMany.models.Player;

@Repository
public interface PlayerRepository extends CrudRepository<Player, Long> {

}
