import React from 'react'
import { Container, Row, Col } from 'reactstrap';
import guigo from '../imgs/guigo.jpg';


export default class Sobre extends React.Component {
    render() {
        return (
            <Container>
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <Row>
                    <Col>
                        <img src={guigo} className="about-img" alt={"Guigo"}></img>
                    </Col>
                    <Col>
                        <div className="about-info">
                            <h1>Guilherme Viegas</h1>
                            <h2>19930425</h2>
                            <h4 className="arial">guilhermeviegas1993@gmail.com</h4>
                            <h4>+55 (48) 996934184</h4>
                            <h2>Brazilian / Portuguese</h2>
                            <h3>Economics - UFSC</h3>
                            <h3>Data Scientist - Aquarela Advanced Analytics</h3>
                            <h4>SkateBoarder, Economist, Data Scientist, R Fanboy, Stats Fanboy, Pastafarian, ...</h4>
                        </div>
                    </Col>
                </Row>
            </Container>
        )
    }
}