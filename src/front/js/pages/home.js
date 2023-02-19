import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Jumbotron } from "../component/Jumbotron";
import { CardConcert } from "../component/CardConcert";

export const Home = () => {
  const { store, actions } = useContext(Context);
//   const concerts = [
//     {
//       name: "nombre1",
//       description: "description1",
//       event_profile_img: "url",
//       establishment_name: "nombre del local",
//       music_genre_event: [1, 2, 3],
//     },
//     {
//       name: "nombre2",
//       description: "description2",
//       event_profile_img: "url",
//       establishment_name: "nombre del local",
//       music_genre_event: [1, 2, 3],
//     },
//   ];

  // console.log(store.concerts)
  return (
    <>
      <Jumbotron />
      <div className="container-fluid seccioneshome">
        <h2>Conciertos</h2>
      </div>
      <div className="d-flex overflow-auto py-5 rowCards">
        {store.concerts?.map((element) => (
			
          <CardConcert
            name={element.name}
            description={element.description}
            event_profile_img={element.event_profile_img}
            establishment_name={element.establishment_name}
            music_genre_event={element.music_genre_event}
          />
        ))}
      </div>
    </>
  );
};
