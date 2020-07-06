"""
LEGION (https://govanguard.com)
Copyright (c) 2020 GoVanguard

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
    version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
    details.

    You should have received a copy of the GNU General Public License along with this program.
    If not, see <http://www.gnu.org/licenses/>.
"""
from db.database import Database


class OSINTRepository:
    def __init__(self, dbAdapter: Database):
        self.dbAdapter = dbAdapter

    def getOSINTByHostIP(self, hostIP):
        query = ('SELECT osint.name, osint.severity, osint.product, osint.version, osint.url, osint.source, '
                 'osint.exploitId, osint.exploit, osint.exploitUrl FROM cve AS osint '
                 'INNER JOIN hostObj AS hosts ON hosts.id = osint.hostId '
                 'WHERE hosts.ip = ?')
        return self.dbAdapter.metadata.bind.execute(query, str(hostIP)).fetchall()
