def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cityDict = dict()

    for city in cities:
        city = city.lower()
        if city in cityDict:
            answer += 1
            cityDict[city] = answer
        else:
            answer += 5
            if len(cityDict) == cacheSize:
                minKey = None
                minVal = 500005
                for key, val in cityDict.items():
                    if val <= minVal:
                        minVal = val
                        minKey = key
                del cityDict[minKey]

            cityDict[city] = answer

    return answer


""" javascript
---------- 내 풀이 ----------
function solution(cacheSize, cities) {
    let answer = 0;
    if(cacheSize === 0) return cities.length *5;
    const cityDict = new Map();
    
    for(let city of cities){
        city = city.toLowerCase();
        if(cityDict.has(city)){
            answer++;
            cityDict.set(city, answer);
        }
        else{
            answer += 5;
            if(cityDict.size === cacheSize){
                let minKey = undefined;
                let minVal = 500005;
                for(let [key, val] of cityDict){
                    if(val <= minVal){
                        minVal = val;
                        minKey = key;
                    }
                }
                cityDict.delete(minKey);
            }
            cityDict.set(city, answer);
        }
    }
    return answer;
}
---------- 인상깊었던 풀이 ----------
function solution(cacheSize, cities) {
    const map = new Map();
    const cacheHit = (city, map) => {
        map.delete(city);
        map.set(city, city);
        return 1;
    };
    const cacheMiss = (city, map, size) => {
        if(size === 0) return 5;
        (map.size === size) && map.delete(map.keys().next().value);
        map.set(city, city);
        return 5;
    };
    const getTimeCache = (city, map, size) => (map.has(city.toLocaleLowerCase()) ? cacheHit : cacheMiss)(city.toLocaleLowerCase(), map, size);
    return cities.map(city => getTimeCache(city.toLocaleLowerCase(), map, cacheSize)).reduce( (a, c) => a + c, 0);
}
"""