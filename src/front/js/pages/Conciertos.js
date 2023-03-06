import React,  {useContext} from "react";
import { CardConcert } from "../component/CardConcert";
import { Jumbotron } from "../component/Jumbotron";
import { Context } from "../store/appContext";


export const Conciertos = () => {
    const { store, actions } = useContext(Context);

  return (
    <>
      <Jumbotron />
      <div className="container ">
        <h2 className="text-center mt-5 mb-5">Conciertos cerca de ti</h2>
        <div className="WrapCards">
          <div className=" d-flex flex-wrap justify-items-center gap-2">
        {store.events?.map((element) => (
            
            <CardConcert
              name={element.name}
              description={element.description}
              event_profile_img={element.event_profile_img}
              establishment_name={element.establishment_name}
              music_genre_event={element.music_genre_event}
              date={element.date}
              hour={element.hour}
              ubicacion={element.ubicacion}
              city = {element.city}
            />
          ))}
          </div>
          </div>
      </div>
    </>
  );
};
