function solution(n, k, enemy) {
    let curr = 0;
    let end = enemy.length-1;

    const getTotalEnemy = (idx)=>{
        if((idx+1)-k >= 0){
            return enemy
            .slice(0, idx+1)
            .sort((a,b)=>a-b)
            .slice(0, (idx+1)-k)
            .reduce((acc,cur)=>acc+cur,0);
        }
        return 0;
    }

    while(true){
        if(curr > end) return end+1;

        const mid = Math.floor((curr + end)/2);
        const totalEnemy = getTotalEnemy(mid);

        if(n-totalEnemy <0){
            end = mid-1;
        }else{
            curr = mid+1;
        }
    }
}