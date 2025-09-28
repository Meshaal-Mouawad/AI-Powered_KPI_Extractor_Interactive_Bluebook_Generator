Mean Time Between Failures (MTBF
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/vb_kpi.vb:1" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/vb_kpi.vb&line=1" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Mean%20Time%20Between%20Failures%20%28MTBF" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>Mean Time Between Failures (MTBF) is a key performance indicator that measures the average time elapsed between failures of a system during its operational period</li><li>It is a critical metric for assessing the reliability and performance of equipment in the oil</li><li>gas</li><li>and petrochemical industries</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of tracking MTBF is to enhance equipment reliability</li><li>minimize downtime</li><li>and improve overall operational efficiency by identifying and addressing failure patterns</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>MTBF is calculated by dividing the total operating hours by the number of failures that occur within that time frame. If there are no failures, the MTBF is equal to the total operating hours.</p>
               <div class="math-equation">$$ \mathrm{MTBF} = \frac{\mathrm{Operating\ Hours}}{\mathrm{Number\ of\ Failures}} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               9.1s (AI 9.1s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 9.062s
                  • AI: 9.062s
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
            <td><ul><li>MTBF is commonly used in conjunction with other reliability metrics such as Mean Time to Repair (MTTR) and Overall Equipment Effectiveness (OEE) to provide a comprehensive view of equipment performance</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The primary inputs for calculating MTBF are the total operating hours of the equipment and the total number of failures experienced during that period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>MTBF is typically expressed in hours, representing the average duration between failures.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for MTBF calculations is usually sourced from maintenance logs, operational reports, and equipment monitoring systems.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher MTBF indicates better reliability and performance of equipment, while a lower MTBF may signal the need for maintenance improvements or equipment upgrades.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: vbnet
      :linenos:
   
      :emphasize-lines: 1
   

      ' KPI: Mean Time Between Failures (MTBF)
   ' Formula: \mathrm{MTBF} = \frac{\mathrm{Operating\ Hours}}{\mathrm{Number\ of\ Failures}}
   Public Module KpiDemo
       Public Function CalcMTBF(operatingHours As Integer, numberOfFailures As Integer) As Double
           If numberOfFailures = 0 Then
               Return operatingHours
           End If
           Return operatingHours / numberOfFailures
       End Function
   End Module