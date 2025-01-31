import React, { useState, useEffect } from 'react'

import { apiPath } from '../../constants/shared'

const useApi = ({ path, params, target, model }) => {
    const [data, setData] = useState({})
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        setIsLoading(true)
        const fetchData = async () => {
            let thisPath = apiPath.concat(path)
            console.log(params)
            // if (target) {
            //     thisPath += `?target=${encodeURIComponent(target)}`;
            // }
            if (params) {
                const queryParams = Object.keys(params)
                    .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`)
                    .join('&');
                thisPath += `?${queryParams}`;
            }
            console.log(thisPath)
            try {
                const response = await fetch(thisPath)
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const result = await response.json();
                console.log(result)
                setData(result.data);
            } catch (err) {
                // setError(err.message);
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();
    }, [path, target, model]); // Re-run the effect if the URL changes

    return {
        data,
        isLoading
    }
}

export default useApi