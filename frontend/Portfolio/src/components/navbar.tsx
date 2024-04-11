import TG from "../assets/tg.svg"
import Github from "../assets/github-mark.svg"

function Navbar() {
  return (
    <>
    <nav>
        <div className="navLinks-container">
            <a href="https://github.com/Trum-ok" title='github' target="_blank"><img src={Github} alt="github" /></a>
            <a href="https://t.me/OpSonata" title='telegram' target="_blank"><img src={TG} alt="telegram" /></a>
            {/* <a href=""><img src="" alt="" /></a> */}
            {/* <img src="" alt=""> </img> */}
        </div>
    </nav>
    </>
  )
}

export default Navbar;