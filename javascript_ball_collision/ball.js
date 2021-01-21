export class Ball {
    constructor(stageWidth, stageHeight, radius, speed) { // 공의 위치가 스테이지에 랜덤으로 위치할 수 있게 클래스 초기함수(class constructor) 정의
        this.radius = radius; // 공의 반지름
        this.vx = speed; // x 축 이동속도
        this.vy = speed; // y 축 이동속도

        const diameter = this.radius * 2; // 공의 지름
        this.x = this.radius + (Math.random() * (stageWidth - diameter)); // x축 랜덤지정
        this.y = this.radius + (Math.random() * (stageHeight - diameter)); // y축 랜덤지정
    }

    draw(ctx, stageWidth, stageHeight) { // 캔버스 context 에 그림을 그릴 수 있는 함수
        this.x += this.vx; // (공의 이전 위치 + 공의 속력) 만큼 좌표가 이동
        this.y += this.vy;

        this.bounceWindow(stageWidth, stageHeight);
        ctx.fillStyle = '#fdd700' // 공의 색깔
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, 2 * Math.PI); // 원을 그리는 함수
        ctx.fill();
    }

    bounceWindow(stageWidth, stageHeight) { // 공이 화면 모서리에 닿으면 반대로 움직이게 하는 함수
        const minX = this.radius; // x, y 좌표의 최소값 최대값은 반지름 길이를 고려해야 함
        const maxX = stageWidth - this.radius;
        const minY = this.radius;
        const maxY = stageHeight - this.radius;

        // 방향전환 조건문
        if (this.x <= minX || this.x >= maxX) { // x 가 최소, 최대값 범위 밖이면 vx 에 -1 을 곱함 '||' 은 or 연산자
            this.vx *= -1;
            this.x += this.vx;
        } else if (this.y <=minY || this.y >= maxY) { // y 가 최소, 최대값 범위 밖이면 vy에 -1을 곱함
            this.vy *= -1;
            this.y += this.vy;
        }
    }
}