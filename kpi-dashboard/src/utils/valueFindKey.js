// 提供方法，通过value反查key

export function valueFindKey(data,value,a,b) {
    const key = data.find(obj=>obj[a] === value)[b]
    return key
}