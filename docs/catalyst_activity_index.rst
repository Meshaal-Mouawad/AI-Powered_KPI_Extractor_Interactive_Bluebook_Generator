Catalyst Activity Index
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/sql_kpi_07.sql:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/sql_kpi_07.sql&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Catalyst%20Activity%20Index" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Catalyst Activity Index measures the proportion of active catalytic sites relative to the total available catalytic sites within a catalyst system</li><li>This index is crucial for assessing the efficiency and effectiveness of catalysts used in various chemical processes</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of the Catalyst Activity Index is to provide a quantitative assessment of catalyst performance</li><li>enabling operators to optimize reaction conditions and improve overall process efficiency</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The Catalyst Activity Index is calculated by dividing the number of active catalytic sites by the total number of catalytic sites, ensuring that division by zero is avoided.</p>
               <p>See code context for implementation details.</p>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.001s
                  • AI: 0.001s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>88.9%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>11.1%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in performance evaluations of catalytic processes</li><li>helping to identify potential improvements in catalyst utilization and longevity</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the count of active catalytic sites and the total count of catalytic sites</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for the Catalyst Activity Index is a dimensionless ratio, expressed as a fraction or percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>The reporting source for this KPI typically comes from laboratory analyses or real-time monitoring systems that assess catalyst performance in operational settings.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher Catalyst Activity Index indicates better catalyst performance, while a lower index may suggest deactivation or inefficiencies that require further investigation.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   
      :emphasize-lines: 1
   

      -- KPI: Catalyst Activity Index
   -- KPI: Catalyst Activity Index
   SELECT active_sites / NULLIF(total_sites,0) AS [Catalyst Activity Index]
   FROM (SELECT 0.87 AS active_sites, 1.0 AS total_sites) t;