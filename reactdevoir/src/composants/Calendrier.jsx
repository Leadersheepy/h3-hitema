const Jours = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche",]

const Calendrier = () => {

    return ( 
    <div className="m-[400px] border">
        <div className="grid grid-cols-7 items-center justify-center text-center">
            <h1>Calendar</h1>

            <div className="col cadre">
                <label>{"<<"}</label>
                <label>Mai</label>
                <label>{">>"}</label>
            </div>

            <div className="col cadre">
                <label>{"<<"}</label>
                <label>2020</label>
                <label>{">>"}</label>
            </div>

            <div className="jourCadre">{Jours.map(jour => (<label>{jour}</label>))}</div>
        
            <div className="days">
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

        </div>
    </div> );
}
 
export default Calendrier;