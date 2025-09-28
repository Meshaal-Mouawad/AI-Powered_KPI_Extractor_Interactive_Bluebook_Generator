Compressor Availability %
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_05.tsql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/tsql_kpi_05.tsql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Compressor%20Availability%20%25" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Compressor Availability % measures the percentage of time that a compressor is operational and available for use compared to the total time it could potentially be operational</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to assess the reliability and efficiency of compressor systems</li><li>ensuring they are available to meet production demands</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The formula calculates the availability percentage by dividing the total uptime hours by the sum of uptime and downtime hours, then multiplying by 100 to express it as a percentage.</p>
               <div class="math-equation">$$ \mathit{Compressor\,Availability\,\%} = \mathit{0))} \times \mathit{100} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.001s
                  • AI: 0.0s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>100.0%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>0.0%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in performance monitoring and maintenance planning for compressor systems within oil</li><li>gas</li><li>and petrochemical operations</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI are the total uptime hours and total downtime hours of the compressor</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for Compressor Availability % is a percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI typically includes operational logs and maintenance records from compressor systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>High compressor availability is crucial for maintaining production efficiency and minimizing operational costs.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Compressor Availability %
   SELECT (uptime_hours / NULLIF(uptime_hours + downtime_hours,0)) * 100 AS [Compressor Availability %]
   FROM (SELECT 720 AS uptime_hours, 24 AS downtime_hours) d;