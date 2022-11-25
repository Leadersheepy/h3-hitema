import Calendrier from "./Calendrier";
import PageRendezVous from './PageRendezVous';
import React, { useEffect } from "react";
import { Route, Routes } from 'react-router-dom';
import { useNavigate } from "react-router-dom";


const RendezVous = () => {

    return ( 
        <div>
            <button className="jolieBouton" href="/meet_form">Nouveau rendez-vous</button>
        </div>
     );
}
 
export default RendezVous;