import React, {useState, useCallback, useEffect} from 'react';

function WeatherTable(props) {
    let latitude = props.latitude;
    let longitude = props.longitude;
    const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&appid=d5b272e4ad18ac7fd4895e21c17a215b`;
    console.log(url)

    const [weather, setWeather] = useState([])

    function pullJson(){
        return     fetch(url)
      .then(response => response.json())
      .then(responseData => {
        console.log(responseData)
        setWeather(responseData)
        })
    }


  useEffect(() => {
       pullJson()
  }, [])

    return <div>
    <h3>Прогноз погоды</h3>
    {
    weather.map( (w) => {
        return <><p>{w.id} {w.title}</p></>
    } )
    }
    </div>;
}

function Location(props) {
  let [latitude, updateLatitude] = useState(0);
  let [longitude, updateLongitude] = useState(0);

  useEffect(() => {
    const status = document.querySelector('#status');
    const mapLink = document.querySelector('#map-link');

    mapLink.href = '';
    mapLink.textContent = '';

    if (!navigator.geolocation) {
        status.textContent = 'Geolocation не поддерживается вашим браузером';
    }
    else
    {
        status.textContent = 'Идет поиск...';
        navigator.geolocation.getCurrentPosition(  function success(position)
    {
        updateLatitude(latitude = position.coords.latitude);
        updateLongitude(longitude = position.coords.longitude);

        status.textContent = '';
        mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
        mapLink.textContent =`Широта: ${position.coords.latitude} °, Долгота: ${position.coords.longitude} °`
    });
  }
   }, []);

  return <>
    <br/>
    <p id = "status"></p>
    Ваше местоположение: <a id = "map-link" target="_blank"></a>
    <WeatherTable latitude={latitude} longitude={longitude}/>
    <br/>
    </>;
}

function App() {

  return (
    <div className="App">
         <Location />
    </div>
  );
}

export default App;
