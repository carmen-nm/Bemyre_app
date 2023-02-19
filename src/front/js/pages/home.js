import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Jumbotron } from "../component/Jumbotron";
import { CardConcert } from "../component/CardConcert";

export const Home = () => {
	const { store, actions } = useContext(Context);

console.log(store.concerts)
	return (
		<>
		<Jumbotron/>
		<div className="container-fluid seccioneshome">
			<h2>Conciertos</h2>		
		</div>
		<div className="row">
			{store.concerts?.map((element)=>{<CardConcert name={element.name} event_profile_img={element.event_profile_img} description={element.description} establishment_name={element.establishment_name} music_genre_event={element.music_genre_event} />})}
		</div>
		
		</>
		
	);
};
