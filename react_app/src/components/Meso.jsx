import React, { useEffect, useState } from "react";
import { Container, Row, Col } from 'reactstrap';

import { cleantxt } from "../fct/cleantxt.js"

export default function Meso() {

    const [query, setQuery] = useState('');

    const inputRef = React.createRef()

    const updateQuery = () => {
        const inputText = inputRef.current.value
        setQuery(inputText)
    }

    const [micror, setMeso] = useState([])
    useEffect(() => {
        fetch(`/get/meso/${query}`).then(response =>
            response.json().then(data => {
                setMeso(data);
            })
        );
    }, [query]);

    return (
        <Container className="meso-cont">
            <Row>
                <Col>
                    <br />
                    <br />
                    <br />
                    <h3>MesoList</h3>
                    <input ref={inputRef} />
                    <button onClick={updateQuery}>Click</button>
                    <br />
                    <ul>
                        {micror.map(m => <li id={cleantxt(m)}>{m}</li>)}
                    </ul>
                </Col>
            </Row>
        </Container>
    );
}

