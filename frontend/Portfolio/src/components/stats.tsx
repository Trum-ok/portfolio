function Stats() {
  return (
    <>
    <div className="block-container" id="stats-block">
        <h1>stats</h1>
        <div className="stat">
            <div className="stat-block" id="github">
                github
            </div>
            <div className="stat-block" id="leetcode">
                leetcode
                <img id="preview" src="https://leetcard.jacoblin.cool/Trum-ok?theme=dark&amp;font=Montserrat&amp;ext=heatmap" />
            </div>
        </div>
    </div>
    </>
  )
}

export default Stats;