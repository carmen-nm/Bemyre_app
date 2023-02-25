import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Jumbotron } from "../component/Jumbotron";
import { CardConcert } from "../component/CardConcert";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container-fluid seccioneshome">
        <h2>Conciertos</h2>

        <div className="rowCards">
          {store.events?.map((element) => (
            <CardConcert
              name={element.name}
              description={element.description}
              event_profile_img={element.event_profile_img}
              establishment_name={element.establishment_name}
              music_genre_event={element.music_genre_event}
              date={element.date}
              ubicacion={element.ubicacion}
              city = {element.city}
            />
          ))}
        </div>
      </div>
    </>
  );
};
