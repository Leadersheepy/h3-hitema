import Calendrier from "./Calendrier";
import React, { useEffect } from "react";
/* import { Route, Routes } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

 */
function RendezVous () {
    return ( 
        <div>
            <Calendrier/>
            
            <button className="jolieBouton" href="/meet_form">Nouveau rendez-vous</button>
        </div>
     );
}
 
export default RendezVous;