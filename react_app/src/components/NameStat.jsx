import React, { useEffect, useState } from "react";
import { Container, Row, Col } from 'reactstrap';

import { cleantxt } from "../fct/cleantxt.js"

export default function NameStat() {

    const [query, setQuery] = useState('');

    const inputRef = React.createRef()

    const updateQuery = () => {
        const inputText = inputRef.current.value
        setQuery(inputText)
    }

    const [namestat, setNamestat] = useState([])
    useEffect(() => {
        fetch(`/namestat/${query}`).then(response =>
            response.json().then(data => {
                // setNamestat(data);
                console.log(data);
            })
        );
    }, [query]);

    return (
        <Container className="namestat-cont">
            <Row>
                <Col>
                    <br />
                    <br />
                    <br />
                    <h3>Namestat</h3>
                    <input ref={inputRef} />
                    <button onClick={updateQuery}>Click</button>
                    <br />
                    <ul>
                        {namestat.map(m => <li id={cleantxt(m)}>{m}</li>)}
                    </ul>
                </Col>
            </Row>
        </Container>
    );
}

