import EnTeteCalendrier from "./EnTeteCalendrier";
import React, {useState, useEffect} from "react";
import CorpsCalendrier from "./CorpsCalendrier";
import RendezVous from "./RendezVous";


function Calendrier() {
    const [annee, setAnnee] = useState();
    const [mois, setMois] = useState();

    const d = new Date();

    function mod(n, m) {
        return ((n % m) + m ) % m;
    }

    function changementDeMois(increment) {
        setMois(mod(mois + increment, 12));
      }
    
      function changementAnnee(increment) {
        setAnnee(annee + increment);
      }

    useEffect(() => {
        setAnnee(d.getFullYear());
        setMois(d.getMonth());
      }, []);

    return ( 
    <div className="m-[400px] border">
        <div className="containerDeux grid grid-cols-7 items-center justify-center text-center">
            <h1>Calendar</h1>
            
            <EnTeteCalendrier mois={mois} annee={annee} changementDeMois={changementDeMois} changementAnnee={changementAnnee}/>
        
            <CorpsCalendrier annee={annee} mois={mois}/>

           {/*  <div className="days">
                <div className="row">
                    <label className="col effet-de-passage pre-date">27</label>
                    <label className="col effet-de-passage pre-date">28</label>
                    <label className="col effet-de-passage pre-date">29</label>
                    <label className="col effet-de-passage pre-date">30</label>
                    <label className="col effet-de-passage">1</label>
                    <label className="col effet-de-passage">2</label>
                    <label className="col effet-de-passage">3</label>
                </div>
                <div className="row">
                    <label className="col effet-de-passage">4</label>
                    <label className="col effet-de-passage">5</label>
                    <label className="col effet-de-passage">6</label>
                    <label className="col effet-de-passage">7</label>
                    <label className="col effet-de-passage">8</label>
                    <label className="col effet-de-passage">9</label>
                    <label className="col effet-de-passage">10</label>
                </div>
                <div className="row">
                    <label className="col effet-de-passage">11</label>
                    <label className="col effet-de-passage">12</label>
                    <label className="col effet-de-passage">13</label>
                    <label className="col effet-de-passage">14</label>
                    <label className="col effet-de-passage">15</label>
                    <label className="col effet-de-passage">16</label>
                    <label className="col effet-de-passage">17</label>
                </div>
                <div className="row">
                    <label className="col effet-de-passage">18</label>
                    <label className="col effet-de-passage">19</label>
                    <label className="col effet-de-passage">20</label>
                    <label className="col effet-de-passage">21</label>
                    <label className="col effet-de-passage">22</label>
                    <label className="col effet-de-passage">23</label>
                    <label className="col effet-de-passage">24</label>
                </div>
                <div className="row">
                    <label className="col effet-de-passage">25</label>
                    <label className="col effet-de-passage">26</label>
                    <label className="col effet-de-passage">27</label>
                    <label className="col effet-de-passage ">28</label>
                    <label className="col effet-de-passage aujourdhui">29</label>
                    <label className="col effet-de-passage">30</label>
                    <label className="col effet-de-passage">31</label>
                </div>    
                <div className="row">
                    <label className="col effet-de-passage post-date">1</label>
                    <label className="col effet-de-passage post-date">2</label>
                    <label className="col effet-de-passage post-date">3</label>
                    <label className="col effet-de-passage post-date">4</label>
                    <label className="col effet-de-passage post-date">5</label>
                    <label className="col effet-de-passage post-date">6</label>
                    <label className="col effet-de-passage post-date">7</label>
                </div>       
            </div>
            </div> */}

        </div>
        </div> );
}
 
export default Calendrier;
