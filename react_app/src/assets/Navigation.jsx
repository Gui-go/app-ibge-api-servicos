import React from 'react'
import { Nav, Navbar, NavbarBrand, NavItem, NavLink } from 'react-bootstrap'
import NavbarToggle from 'react-bootstrap/esm/NavbarToggle'
import NavbarCollapse from 'react-bootstrap/esm/NavbarCollapse'
import LinkedInIcon from '@material-ui/icons/LinkedIn';
import FacebookIcon from '@material-ui/icons/Facebook';
import InstagramIcon from '@material-ui/icons/Instagram';
import GitHubIcon from '@material-ui/icons/GitHub';
import TwitterIcon from '@material-ui/icons/Twitter';
import WhatsAppIcon from '@material-ui/icons/WhatsApp';
import ReactTooltip from 'react-tooltip';

export const Navigation = () => (
    <div>
        <ReactTooltip className="tooltip" />
        <Navbar className="navbar" expand="lg">
            <NavbarBrand href="/">Guigo's APP </NavbarBrand>
            <NavbarToggle aria-controls="basic-navbar-nav" />
            <NavbarCollapse id="basic-navbar-nav">
                <Nav> {/*className="ml-auto"*/}
                    {/* <NavItem><NavLink href="/">Home</NavLink></NavItem> */}
                    <NavItem><NavLink href="/home">Home</NavLink></NavItem>
                    <NavItem><NavLink href="/micro">Micro</NavLink></NavItem>
                    <NavItem><NavLink href="/meso">Meso</NavLink></NavItem>
                    <NavItem><NavLink href="/namestat">NameStat</NavLink></NavItem>
                    <NavItem><NavLink href="/malha">Malha</NavLink></NavItem>
                    <NavItem><NavLink href="/mapa">Mapa</NavLink></NavItem>
                    <NavItem><NavLink href="/about">About</NavLink></NavItem>
                </Nav>
                <Nav className="ml-auto">
                    <h6>Flags</h6>
                    <NavItem><a href="https://github.com/Gui-go/" target="blank"><GitHubIcon className="nav-icon" fontSize='large' /></a></NavItem>
                    <NavItem><a href="https://www.linkedin.com/in/guilherme-viegas-1b5b0495/" target="blank"><LinkedInIcon className="nav-icon" fontSize='large' /></a></NavItem>
                    <NavItem><a href="https://www.facebook.com/guilherme.viegas.90" target="blank"><FacebookIcon className="nav-icon" fontSize='large' /></a></NavItem>
                    <NavItem><a href="https://www.instagram.com/gui.go.13/" target="blank"><InstagramIcon className="nav-icon" fontSize='large' /></a></NavItem>
                    <NavItem><a href="/" target="blank"><WhatsAppIcon className="nav-icon" fontSize='large' data-tip='+55 (48) 996934184' /></a></NavItem>
                    <NavItem><a href="/" target="blank"><TwitterIcon className="nav-icon" fontSize='large' data-tip="He doesn't really use twitter" /></a></NavItem>
                </Nav>
            </NavbarCollapse>
        </Navbar>
    </div>
)
