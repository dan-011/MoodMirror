import './navbar.css';
import { Link, useMatch, useResolvedPath } from "react-router-dom"

function Navbar() {
    return <nav className="nav">
        <Link to="/" className="site-title">Mood Mirror</Link>
        <ul>
            <NavLink to="/model">Model</NavLink>
            <NavLink to="/about">About</NavLink>
        </ul>
    </nav>
}

function NavLink({ to, children, ...props }) {
    const resolvedPath = useResolvedPath(to);
    const isActive = useMatch({ path: resolvedPath.pathname, end: true});
    return (
        <li className={isActive ? "active" : ""}>
            <Link to={to} {...props}>
                {children}
            </Link>
        </li>
    )
}

export default Navbar;