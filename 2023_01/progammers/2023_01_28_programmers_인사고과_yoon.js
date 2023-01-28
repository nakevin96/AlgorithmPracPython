function solution(scores) {
    const wanhoScore = [scores[0][0], scores[0][1]];
    const wanhoScoreSum = scores[0][0] + scores[0][1];
    scores = scores
        .filter((item) => item[0] + item[1] >= wanhoScoreSum)
        .sort((a, b) => a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]);

    let maxPeerScore = -1;
    let ranking = 1;
    for (let score of scores) {
        if (wanhoScore[0] < score[0] && wanhoScore[1] < score[1]) return -1;
        if (maxPeerScore <= score[1]) {
            if (wanhoScoreSum < score[0] + score[1]) {
                ranking += 1;
            }
            maxPeerScore = score[1]
        }
    }
    return ranking;
}
