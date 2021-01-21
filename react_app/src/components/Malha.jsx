import React, { useEffect, useState } from "react";
import { Container, Row, Col } from 'reactstrap';

export default function Malha() {

    const [query, setQuery] = useState('');

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
                    <h3>Malha</h3>
                    <input ref={inputRef} />
                    <button onClick={updateQuery}>Click</button>
                    <br />
                    <h2>{ typeof malha }</h2>
                </Col>
            </Row>
        </Container>
    );
}

