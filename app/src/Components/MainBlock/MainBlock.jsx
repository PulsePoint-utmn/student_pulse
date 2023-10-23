import "./MainBlock.css"
function MainBlock() {
    return ( 
        <div className="h-screen md:h-1/2screen bg-gradient-to-r from-sky-500 to-indigo-500">
            <div className="flex flex-col md:flex-row-reverse place-content-center">
                {/*<div className="coolpic">cool pic</div>*/}
                <div className="text mont-bold flex flex-col">
                    <span className="pb-1 md:text-5xl text-3xl">Простой способ общения со студентами</span>
                    <span className="md:text-xl text-xl">„Прекрасная вещь — общение с мудрецом.“</span>
                </div>
            </div>
            <button className="mt-6 bg-white text-black rounded-full mx-auto">Создать форму</button>
        </div>
     );
}

export default MainBlock;