// import React from 'react'
import React, { useEffect, useState } from "react";
import { Container, Row, Col } from 'reactstrap';


import { cleantxt } from "../fct/cleantxt.js"

export default function Micro() {

    const [query, setQuery] = useState('');

    const inputRef = React.createRef()

    const updateQuery = () => {
        const inputText = inputRef.current.value
        setQuery(inputText)
    }

    const [micror, setMicror] = useState([])
    useEffect(() => {
        fetch(`/get/micro/${query}`).then(response =>
            response.json().then(data => {
                setMicror(data);
            })
        );
    }, [query]);

    return (
        <Container className="art-cont">
            <Row>
                <Col>
                    <br />
                    <br />
                    <br />
                    <h3>MicroList</h3>
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

