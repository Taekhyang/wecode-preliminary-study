import {
    Ball
} from "./ball.js";


class App {
    constructor() {
        // 자바스크립트 constructor 는 App instance 가 생성될 때 변수들의 데이터값을 초기화, 파이썬의 __init__ 메소드와 비슷한 역할
        // this 역시 파이썬의 self 와 비슷한 역할
        this.canvas = document.createElement('canvas'); // canvas object 생성
        this.ctx = this.canvas.getContext('2d');

        document.body.appendChild(this.canvas); // canvas 를 html body 에 삽입

        window.addEventListener('resize', this.resize.bind(this), false);
        this.resize();

        this.ball = new Ball(this.stageWidth, this.stageHeight, 60, 15); // 공의 사이즈와 움직이는 스피드 세팅

        window.requestAnimationFrame(this.animate.bind(this)); // 공을 화면에 끊임없이 계속 그려주는 역할
    }

    resize() {
        // 스크린 사이즈는 가변적이기 때문에 사이즈를 조정하는 함수를 생성
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        this.canvas.width = this.stageWidth * 2;
        this.canvas.height = this.stageHeight * 2;
        this.ctx.scale(2, 2);
    }

    animate(t) { // 애니메이션을 실제로 구동시키는 함수
        window.requestAnimationFrame(this.animate.bind(this));

        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight); // 공이 이동한 이전 프레임을 지움

        this.ball.draw(this.ctx, this.stageWidth, this.stageHeight) // 공의 위치를 그려줌
    }
}

window.onload = () => {
    new App();
}