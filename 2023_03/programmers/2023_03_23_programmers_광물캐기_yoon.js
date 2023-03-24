// https://school.programmers.co.kr/learn/courses/30/lessons/172927

// 광물에 점수를 부여해서 가장 피로도가 높은 광물그룹에 좋은 곡괭이 할당

function solution(picks, minerals) {
    const total_picks = picks.reduce((a, b) => a + b, 0);
    if (total_picks * 5 < minerals.length) {
        minerals = minerals.slice(0, total_picks * 5)
    }
    const pickMineralDict = {
        'diamond': [1, 1, 1],
        'iron': [5, 1, 1],
        'stone': [25, 5, 1],
    };
    const mineral_groups = [];
    for (let i = 0; i < Math.ceil(minerals.length / 5); i++) {
        mineral_groups.push(minerals.slice(i * 5, (i + 1) * 5));
    }
    const compareMineralGroups = (aGroup, bGroup) => {
        let aSum = [0, 0, 0];
        for (let a of aGroup) {
            aSum[0] += 1;
            if (a === 'diamond') {
                aSum[1] += 5;
                aSum[2] += 25;
            } else if (a === 'iron') {
                aSum[1] += 1;
                aSum[2] += 5;
            } else {
                aSum[1] += 1;
                aSum[2] += 1;
            }
        }
        let bSum = [0, 0, 0];
        for (let b of bGroup) {
            bSum[0] += 1;
            if (b === 'diamond') {
                bSum[1] += 5;
                bSum[2] += 25;
            } else if (b === 'iron') {
                bSum[1] += 1;
                bSum[2] += 5;
            } else {
                bSum[1] += 1;
                bSum[2] += 1;
            }
        }
        if (aSum[2] !== bSum[2]) {
            return bSum[2] - aSum[2];
        } else if (aSum[1] !== bSum[1]) {
            return bSum[1] - aSum[1];
        } else {
            return bSum[0] - aSum[0];
        }
    }
    let result = 0;
    const getFatigue = (pickName, mineralName) => {
        if (mineralName === 'diamond') {
            return pickMineralDict[pickName][0];
        } else if (mineralName === 'iron') {
            return pickMineralDict[pickName][1];
        } else {
            return pickMineralDict[pickName][2];
        }
    }

    mineral_groups.sort(compareMineralGroups);
    for (let mg of mineral_groups) {
        let selectedPick;
        if (picks[0] > 0) {
            selectedPick = 'diamond';
            picks[0] -= 1
        } else if (picks[1] > 0) {
            selectedPick = 'iron';
            picks[1] -= 1
        } else {
            selectedPick = 'stone';
            picks[2] -= 1
        }
        for (let m of mg) {
            result += getFatigue(selectedPick, m);
        }
    }
    return result;
}