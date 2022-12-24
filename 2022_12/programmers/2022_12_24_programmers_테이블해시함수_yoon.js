function solution(data, col, row_begin, row_end) {
    const result = [];
    data.sort((a,b)=>{
        if(a[col-1]===b[col-1]) return b[0]-a[0];
        return a[col-1]-b[col-1];
    });
    for(let idx=row_begin; idx<=row_end; idx++){
        let s_i = data[idx-1].reduce((acc,cur)=>acc+(cur%(idx)),0);
        result.push(s_i);
    }
    return result.reduce((acc, cur)=>acc^cur);
}