from database.DB_connect import DBConnect
from model.edge import Edge
from model.nation import Nation


class DAO:

    @staticmethod
    def getAllNations():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result=[]

        query = """ Select *
                     from country c"""
        cursor.execute(query)

        for row in cursor:
            result.append(Nation(row['StateAbb'], row['CCode'], row['StateNme']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(anno, idMap):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        if int(anno)<2006:
            query="""select c.state1no, c.state2no  
                    from contiguity c
                    where c.`year` <= %s """
            cursor.execute(query, (anno,))
            for row in cursor:
                if idMap[row['state1no']] not in result:
                    result.append(idMap[row['state1no']])
                if idMap[row['state2no']] not in result:
                    result.append(idMap[row['state2no']])
        else:
            query1 = """select c.state1no, c.state2no  
                    from contiguity c
                    where c.`year` <= %s """
            cursor.execute(query1,(anno,))
            for row in cursor:
                if idMap[row['state1no']] not in result:
                    result.append(idMap[row['state1no']])
                if idMap[row['state2no']] not in result:
                    result.append(idMap[row['state2no']])
            query2 = """select c.state1no, c.state2no  
                        from contiguity2006 c"""
            cursor.execute(query2)
            for row in cursor:
                if idMap[row['state1no']] not in result:
                    result.append(idMap[row['state1no']])
                if idMap[row['state2no']] not in result:
                    result.append(idMap[row['state2no']])


        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllEdges(anno, idMap):

        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        if int(anno) < 2006:
            query = """select c.state1no, c.state2no 
                        from contiguity c 
                        where c.`year` <= %s
                        and c.conttype = 1 """
            cursor.execute(query, (anno,))
            for row in cursor:
                result.append(Edge(idMap[row['state1no']],idMap[row['state2no']]))

        else:
            query1 = """select c.state1no, c.state2no 
                        from contiguity c 
                        where c.`year` <= %s
                        and c.conttype = 1 """
            cursor.execute(query1, (anno,))
            for row in cursor:
                result.append(Edge(idMap[row['state1no']], idMap[row['state2no']]))

            query2 = """select c.state1no, c.state2no  
                        from contiguity2006 c
                        where c.conttype = 1"""
            cursor.execute(query2)
            for row in cursor:
                result.append(Edge(idMap[row['state1no']], idMap[row['state2no']]))


        cursor.close()
        conn.close()

        return result



