import "./MainBlock.css"
function MainBlock() {
    return ( 
        <div className="main  h-96 bg-black">
            <div className="flex flex-col md:flex-col place-content-center">
                {/*<div className="coolpic">cool pic</div>*/}
                    <span className="pb-1 md:text-5xl text-3xl ">Простой способ общения со студентами</span>

            </div>
            <button className="bg-white text-black rounded-full mx-auto">Создать форму</button>
        </div>
     );
}

export default MainBlock;