'''javascript
function solution(target) {
    const [THROW_COUNT, VALID_COUNT] = [0, 1]
    let validTable = Array.from({length: 20}, (v,i)=> i+1);
    validTable.push(50);
    const invalidTable = Array.from(new Set([...Array.from({length: 20}, (v,i)=>(i+1)*2).filter(item=>item>20), ...Array.from({length:20}, (v,i)=>(i+1)*3).filter(item=>item>20)]));

    const dt = Array.from({length: target+1}, ()=> new Array(Infinity, 0));
    dt[0][THROW_COUNT] = 0;

    for(let targetVal= 1; targetVal<=target; targetVal++){
        for(const v of validTable){
            if((targetVal-v)<0) continue;

            let tmpThrow = dt[targetVal-v][THROW_COUNT] + 1;
            let tmpValid = dt[targetVal-v][VALID_COUNT] + 1;

            if(tmpThrow < dt[targetVal][THROW_COUNT]){
                dt[targetVal] = [tmpThrow, tmpValid];
            }else if(tmpThrow === dt[targetVal][THROW_COUNT]){
                dt[targetVal][VALID_COUNT] = Math.max(tmpValid, dt[targetVal][VALID_COUNT]);
            }
        }
        for(const iv of invalidTable){
            if((targetVal-iv)<0) continue;

            let tmpThrow = dt[targetVal-iv][THROW_COUNT] + 1;
            let tmpValid = dt[targetVal-iv][VALID_COUNT];

            if(tmpThrow < dt[targetVal][THROW_COUNT]){
                dt[targetVal] = [tmpThrow, tmpValid];
            }
        }
    }

    return dt[target]
}
'''
import math


def solution(target):
    THROW_COUNT, VALID_COUNT = 0, 1
    valid_table = [i for i in range(1, 21)]
    valid_table.append(50)
    invalid_table = [i * 2 for i in range(1, 21) if i * 2 > 20]
    invalid_table.extend([i * 3 for i in range(1, 21) if i * 3 > 20])
    invalid_table = list(set(invalid_table))

    dt = [[math.inf, 0] for _ in range(target + 1)]
    dt[0][THROW_COUNT] = 0

    for t in range(1, target + 1):
        for v in valid_table:
            if t - v < 0:
                continue

            tmp_throw = dt[t - v][THROW_COUNT] + 1
            tmp_valid = dt[t - v][VALID_COUNT] + 1

            if tmp_throw < dt[t][THROW_COUNT]:
                dt[t] = [tmp_throw, tmp_valid]
            elif tmp_throw == dt[t][THROW_COUNT]:
                dt[t][VALID_COUNT] = max(tmp_valid, dt[t][VALID_COUNT])

        for iv in invalid_table:
            if t - iv < 0:
                continue

            tmp_throw = dt[t - iv][THROW_COUNT] + 1
            tmp_valid = dt[t - iv][VALID_COUNT]

            if tmp_throw < dt[t][THROW_COUNT]:
                dt[t] = [tmp_throw, tmp_valid]

    return dt[target]
