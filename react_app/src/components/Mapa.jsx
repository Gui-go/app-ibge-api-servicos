import React, { useEffect, useState } from "react";
import { Container, Row, Col } from 'reactstrap';
// import { Map, Marker, Popup, TileLayer } from "react-leaflet";
// import Axios from 'axios';
// import { MapContainer, TileLayer, Polygon, GeoJSON } from 'react-leaflet';




export default function Mapa() {

    // const polygon = [
    //     [11.515, -10.09],
    //     [51.52, -0.1],
    //     [31.52, -20.12],
    // ]


    const [query, setQuery] = useState('4205407');

    const inputRef = React.createRef()

    const updateQuery = () => {
        const inputText = inputRef.current.value
        setQuery(inputText)
    }

    const [malha, setMalha] = useState([])
    useEffect(() => {
        fetch(`/malha/${query}`).then(response =>
            response.json().then(data => {
                setMalha(data);
                console.log(data['features']);
            })
        );
    }, [query]);

    return (
        <Container className="mapa-cont">
            <Row>
                <Col>
                    <br />
                    <br />
                    <br />
                    <h3>Map</h3>
                    <input ref={inputRef} />
                    <button onClick={updateQuery}>Click</button>
                    <br />
                    <h1>{typeof malha}</h1>
                </Col>
            </Row>
            {/* <MapContainer
                className="markercluster-map"
                center={[51.0, 19.0]}
                zoom={4}
                maxZoom={18}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                <Polygon positions={polygon} />
                <GeoJSON data={malha} />
            </MapContainer> */}
        </Container>
    );
}

// 4205407